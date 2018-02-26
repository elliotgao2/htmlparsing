# HTML Parsing

Pure HTML parsing library.

## Installation

```python
pip install htmlparsing

# or

pip install git+https://github.com/gaojiuli/htmlparsing
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
e.links
"""
{...'/users/membership/', '/events/python-events', '//docs.python.org/3/tutorial/controlflow.html#defining-functions'}
"""
e.absolute_links
"""
{...'https://python.org/download/alternatives',  'https://python.org/about/success/#software-development', 'https://python.org/download/other/', 'https://python.org/community/irc/'}
"""

# Selectors and get attrs
e.xpath('//a')[0].attrs
"""{'href': '#content', 'title': 'Skip to content'}"""

e.xpath('//a')[0].attrs.title
"""Skip to content"""

e.css('a')[0].attrs
"""{'href': '#content', 'title': 'Skip to content'}"""

e.parse('<a href="#content" title="Skip to content">{}</a>')
"""<Result ('Skip to content',) {}>"""

# Get content or html
e.xpath('//a')[5].text
"""PyPI"""

e.xpath('//a')[5].html
"""<a href="https://pypi.python.org/" title="Python Package Index">PyPI</a>"""

e.xpath('//a')[5].markdown
"""[PyPI](https://pypi.python.org/ "Python Package Index")"""

```
