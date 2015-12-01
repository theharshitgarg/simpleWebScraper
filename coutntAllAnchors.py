from bs4 import BeautifulSoup
import urllib2
def countAnchors(url):
	html_page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html_page,"lxml")
	  	 
	return len(soup.find_all('a'))	

print countAnchors(url = "http://www.pythonforbeginners.com")	
