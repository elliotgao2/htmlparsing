# HTML Parsing

No Pain HTML parsing library. A wrapper of lxml.


## Installation

```python
pip install htmlparsing

# or

pip install git+https://github.com/gaojiuli/htmlparsing
```

## Usage

```python
import requests

url = 'https://python.org'
r = requests.get(url)

# Init

from htmlparsing import Element
e = Element(text=r.text, base_url=url)

# Usage

e.links
e.absolute_links
e.xpath('//a')[0].attrs
e.xpath('//a')[0].attrs.title
e.css('a')[0].attrs
e.parse('<a href="#content" title="Skip to content">{}</a>')
e.css('a')[5].text
e.css('a')[5].html
e.css('a')[5].markdown

```
