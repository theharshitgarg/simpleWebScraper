from lxml import html
import requests

base_url = 'http://econpy.pythonanywhere.com/ex/00{}.html'
print base_url, base_url.format(1)
for i in range(1,6):
	page = requests.get(base_url.format(1))
	#print page
	#"""
	tree = html.fromstring(page.content)
	#print tree
	#print tree.content
	#print page.content
	print "Customer listed on page {}".format(i)
	#This will create a list of buyers:
	buyers = tree.xpath('//div[@title="buyer-name"]/text()')
	#This will create a list of prices
	prices = tree.xpath('//span[@class="item-price"]/text()')
	print 'Buyers: ', buyers
	print 'Prices: ', prices
	print "-"*60
#"""
