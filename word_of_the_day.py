from urllib2 import urlopen
from bs4 import BeautifulSoup
import re


def get_word():
	regex = re.compile("[\<\[].*?[\>\]]")

	URL = 'https://www.danishclass101.com/danish-phrases/'

	page = BeautifulSoup(urlopen(URL), features="lxml")

	danish_div = page.find_all("div" , class_="r101-wotd-widget__word")
	english_div = page.find_all("div" , class_="r101-wotd-widget__english")

	danish = []
	english = []

	for x, y in zip(danish_div, english_div):
		danish.append(re.sub(regex, "", str(x)))
		english.append(re.sub(regex, "", str(y)))

	return danish, english




'''
for x in danish_div:
	print (re.sub(regex, "", str(x)))

for x in english_div:
	print (re.sub(regex, "", str(x)))
'''