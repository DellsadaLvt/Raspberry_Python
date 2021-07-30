import urllib.request
import lxml.etree
from lxml.cssselect import CSSSelector

url= "http://weather.yahoo.com/united-states/illinois/chicago-2379574/"
# establish http connection with the remote website
response= urllib.request.urlopen(url)
# retrieve the html code
html= response.read()


#define encoding want to conver from the raw binary of html
encoding= lxml.etree.HTMLParser(encoding="utf-8")
# fromstring produce a list that constain the string of all variables of html
doctree= lxml.etree.fromstring(html, encoding)

span= CSSSelector("span.num")
temp= span(doctree)[0].text
print(temp)


