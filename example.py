import requests

from htmlparsing import Element, HTMLParsing, Text, Attr, Parse

url = 'https://python.org/'
r = requests.get(url)

# init
e = Element(text=r.text)

# Get links
print(e.links)
"""
{...'/users/membership/', '/events/python-events', '//docs.python.org/3/tutorial/controlflow.html#defining-functions'}
"""
print(e.absolute_links)
"""
{...'https://python.org/download/alternatives',  'https://python.org/about/success/#software-development', 'https://python.org/download/other/', 'https://python.org/community/irc/'}
"""

# Selectors and get attrs
print(e.xpath('//a')[0].attrs)
"""{'href': '#content', 'title': 'Skip to content'}"""

print(e.xpath('//a')[0].attrs.title)
"""Skip to content"""

print(e.css('a')[0].attrs)
"""{'href': '#content', 'title': 'Skip to content'}"""

print(e.parse('<a href="#content" title="Skip to content">{}</a>')[0])
"""<Result ('Skip to content',) {}>"""

# Get content or html
print(e.xpath('//a')[5].text)
"""PyPI"""

print(e.xpath('//a')[5].html)
"""<a href="https://pypi.python.org/" title="Python Package Index">PyPI</a>"""

print(e.xpath('//a')[5].markdown)
"""[PyPI](https://pypi.python.org/ "Python Package Index")"""

url = 'https://news.ycombinator.com/'
r = requests.get(url)
article_list = HTMLParsing(r.text).list('.athing', {'title': Text('a.storylink'),
                                                    'link': Attr('a.storylink', 'href')})
print(article_list)

url = 'https://news.ycombinator.com/item?id=16476454'
r = requests.get(url)
article_detail = HTMLParsing(r.text).detail({'title': Text('a.storylink'),
                                             'points': Parse('span.score', '>{} points'),
                                             'link': Attr('a.storylink', 'href')})
print(article_detail)


from setuptools import find_packages, setup

setup(
    name="htmlparsing",
    version="0.1.0",
    description="Pure HTML parsing library.",
    author="Jiuli Gao",
    author_email="gaojiuli@gmail.com",
    url='https://github.com/gaojiuli/htmlparsing',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    py_modules=['htmlparsing'],
    include_package_data=True,
    zip_safe=False,
)
