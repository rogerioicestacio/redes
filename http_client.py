from lxml import html
import requests

page = requests.get('http://www.uol.com.br')
tree = html.fromstring(page.content)

for tags in page.headers:
    print tags,' : ',page.headers[tags]


