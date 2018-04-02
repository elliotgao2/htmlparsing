from collections import defaultdict
from typing import Dict

import html2text
from lxml import html
from parse import findall
from parse import search as parse_search


class Element:

    def __init__(self, text: str):
        self.html = text
        self.element = html.fromstring(text)

    def __repr__(self):
        return '<Element {}>'.format(self.element.tag)

    @property
    def markdown(self):
        return html2text.html2text(self.html)

    @property
    def text(self):
        return ''.join(self.element.xpath('//text()'))

    @property
    def attrs(self):
        r = defaultdict(str)
        r.update(self.element.items())
        return r

    @property
    def links(self):
        return set([e.attrs.get('href') for e in self.css('a') if e.attrs.get('href') is not None])

    def absolute_links(self, base_url):
        return set(['{}/{}'.format(base_url.strip('/'), link.lstrip('/')) for link in self.links if ':' not in link])

    def parse(self, template: str):
        return parse_search(template, self.html)[0]

    def parse_all(self, template: str):
        return [r[0] for r in findall(template, self.html)]

    def css(self, selector: str):
        return [Element(html.tostring(e).decode().strip()) for e in self.element.cssselect(selector)]

    def xpath(self, selector: str):
        return [Element(html.tostring(e).decode().strip()) for e in self.element.xpath(selector)]


class HTML:
    def __init__(self, text: str):
        self.html = text
        self.element = Element(text)

    def detail(self, fields: Dict[str, str]):
        results = {}
        for field, selector in fields.items():
            try:
                e = self.element.css(selector)[0]
                result = {'text': e.text,
                          'href': e.attrs['href'],
                          'title': e.attrs['title'],
                          'src': e.attrs['src']}
                if result.get('src'):
                    result['type'] = 'image'
                elif result.get('href'):
                    result['type'] = 'link'
                else:
                    result['type'] = 'text'
                results[field] = result
            except:
                pass
        return results

    def list(self, selector: str, fields: Dict[str, str]):
        return [HTML(e.html).detail(fields) for e in self.element.css(selector)]
