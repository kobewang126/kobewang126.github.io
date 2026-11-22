"""Check deployable pages, local resources, anchors, and translation coverage."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text()
js = (root / 'i18n.js').read_text()
translations = json.loads(js.split('const translations = ', 1)[1].split(';', 1)[0])

class Check(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.anchors = []
        self.qr_count = 0
        self.projects = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids
            self.ids.add(attrs['id'])
        for attr in ('src', 'href'):
            value = attrs.get(attr, '')
            if not value or value.startswith(('https:', 'mailto:')):
                continue
            if value.startswith('#'):
                self.anchors.append(value[1:])
            else:
                assert (root / value).is_file(), value
        if tag == 'img' and attrs.get('src') == 'assets/wechat-qrcode.jpg':
            self.qr_count += 1
        if tag == 'a' and ('card' in attrs.get('class', '').split() or 'tool' in attrs.get('class', '').split()):
            self.projects += 1
        for name in ('alt', 'aria-label'):
            value = attrs.get(name, '')
            if re.search('[\u4e00-\u9fff]', value) and value != '语言 / Language':
                assert value in translations, value

    def handle_data(self, value):
        value = value.strip()
        if re.search('[\u4e00-\u9fff]', value) and value != '中文':
            assert value in translations, value

check = Check()
check.feed(html)
assert all(anchor in check.ids for anchor in check.anchors)
assert check.qr_count == 1
assert check.projects == 7
assert '设计草案' not in html and '概念稿' not in html
ET.parse(root / 'sitemap.xml')
for path in (root / 'assets').glob('*.svg'):
    ET.parse(path)
print('Passed: 7 projects, 1 QR code, local assets, section links, translations, sitemap, SVGs.')
