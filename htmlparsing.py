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

    def __init__(self, text, base_url=''):
        self.html = text
        self.base_url = base_url.strip('/')
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

    @property
    def absolute_links(self):
        results = []
        for link in self.links:
            if ':' not in link:
                if link.startswith('/'):
                    href = '{}{}'.format(self.base_url, link)
                else:
                    href = '{}/{}'.format(self.base_url, link)
                results.append(href)
        return set(results)

    def parse(self, template):
        return parse_search(template, self.html)

    def parse_all(self, template):
        return [r for r in findall(template, self.html)]

    def css(self, selector):
        return [Element(html.tostring(e).decode('utf-8'), self.base_url) for e in self.element.cssselect(selector)]

    def xpath(self, selector):
        return [Element(html.tostring(e).decode('utf-8'), self.base_url) for e in self.element.xpath(selector)]
