from typing import Dict

import html2text
from lxml import html
from parse import findall
from parse import search as parse_search


class AttributeDict(dict):
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value


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
        return AttributeDict(self.element.items())

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


class Selector:
    def __init__(self, selector: str):
        self.selector = selector

    def parse(self, element: Element):
        raise NotImplemented


class Text(Selector):
    def parse(self, element: Element):
        return element.css(self.selector)[0].text


class Attr(Selector):
    def __init__(self, selector: str, attr: str):
        super().__init__(selector)
        self.attr = attr

    def parse(self, element: Element):
        return element.css(self.selector)[0].attrs[self.attr]


class HTML(Selector):
    def parse(self, element: Element):
        return element.css(self.selector)[0].html


class Markdown(Selector):
    def parse(self, element: Element):
        return element.css(self.selector)[0].markdown


class Parse(Selector):
    def __init__(self, selector: str, template: str, many: bool = False):
        super().__init__(selector)
        self.template = template
        self.many = many

    def parse(self, element: Element):
        if self.many:
            return element.css(self.selector)[0].parse_all(self.template)
        else:
            return element.css(self.selector)[0].parse(self.template)


class HTMLParsing:
    def __init__(self, text: str):
        self.html = text
        self.element = Element(text)

    def detail(self, fields: Dict[str, Selector]):
        return {field: selector.parse(self.element) for field, selector in fields.items()}

    def list(self, selector: str, fields: Dict[str, Selector]):
        return [HTMLParsing(e.html).detail(fields) for e in self.element.css(selector)]
