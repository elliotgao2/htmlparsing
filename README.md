# HTML Parsing: Pure HTML parsing library.

## Installation

only support python3.

```python
pip install htmlparsing
```

## Usage

```python
import requests

from htmlparsing import Element

url = 'https://python.org'
r = requests.get(url)

# init
e = Element(text=r.text, base_url=url)

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

print(e.parse('<a href="#content" title="Skip to content">{}</a>'))
"""<Result ('Skip to content',) {}>"""

# Get content or html
print(e.xpath('//a')[5].text)
"""PyPI"""

print(e.xpath('//a')[5].html)
"""<a href="https://pypi.python.org/" title="Python Package Index">PyPI</a>"""

print(e.xpath('//a')[5].markdown)
"""[PyPI](https://pypi.python.org/ "Python Package Index")"""

```
