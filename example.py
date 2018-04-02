from pprint import pprint

import requests

from htmlparsing import HTML

url = 'https://www.v2ex.com/'
r = requests.get(url)
article_list = HTML(r.text).list('.cell.item', {'title': '.item_title a',
                                                'node': 'a.node',
                                                'avatar': '.avatar',
                                                'count': '.count_livid',
                                                'author': 'strong a'})

pprint(article_list)
