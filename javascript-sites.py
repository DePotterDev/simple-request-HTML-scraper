from requests_html import HTMLSession

session = HTMLSession()

url = 'https://www.pichau.com.br/hardware/ssd'

r = session.get(url)

products = r.html.find('.product-item-link')
prices = r.html.find('.price-boleto span')

productlist = []
pricelist = []

total = {
    'product': productlist,
    'price': pricelist
    }

for index, product in enumerate(products):
    item = product.text
    productlist.append(item)

for index, price in enumerate(prices):
    item = price.text
    pricelist.append(item[8:])

print(total)