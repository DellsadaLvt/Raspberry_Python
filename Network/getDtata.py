import urllib.request
import lxml.etree
from lxml.cssselect import CSSSelector

url= "http://weather.yahoo.com/united-states/illinois/chicago-2379574"
response= urllib.request.urlopen(url)
html= response.read()
print(html)
