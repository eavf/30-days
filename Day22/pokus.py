import requests_html

s = requests_html.HTMLSession()

url = 'https://stackoverflow.com/questions/tagged/python?tab=Votes'
#url = 'http://books.toscrape.com/'
r = s.get(url)

find_elements = r.html.find('a img')
find_elements = r.html.find('div.s-post-summary')

look_attr = 'alt'
look_attr = 'data-post-id'

for item in find_elements:
    print('data-post-id:', item.attrs[look_attr])