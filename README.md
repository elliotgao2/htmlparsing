# HTML Parsing

No Pain HTML parsing library.


## Installation

```python
pip install htmlparsing
```

## Usage


### Parse list

```python
import requests
from htmlparsing import Element, HTMLParsing, Text, Attr, Parse, HTML, Markdown

url = 'https://news.ycombinator.com/'
r = requests.get(url)
article_list = HTMLParsing(r.text).list('.athing', {'title': Text('a.storylink'), # css selector
                                                    'link': Attr('a.storylink', 'href')})
print(article_list)

```
### Parse detail

```python
import requests
from htmlparsing import Element, HTMLParsing, Text, Attr, Parse

url = 'https://news.ycombinator.com/item?id=16476454'
r = requests.get(url)
article_detail = HTMLParsing(r.text).detail({'title': Text('a.storylink'),
                                             'points': Parse('span.score', '>{} points'),
                                             'link': Attr('a.storylink', 'href')})
print(article_detail)
```

### Element

```python

import requests
from htmlparsing import Element
url = 'https://python.org/'
r = requests.get(url)

e = Element(text=r.text)
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
