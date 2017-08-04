import requests
from bs4 import BeautifulSoup
import os
import socket
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
socket.setdefaulttimeout(2.0)
import urllib


if __name__ == '__main__':
	url = 'http://dianying.2345.com/mingxing/list/'
	res = requests.get(url)
	#res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text, 'html.parser')
	part1 = soup.find_all('div',class_="v_picConBox mt15")[0]
	img_list = part1.find_all('img')
	#author_list = part1.find_all('span', class_="sTit")



	_path = os.getcwd()
	new_path = os.path.join(_path, 'star_data')
	if not os.path.isdir(new_path):
	    os.mkdir(new_path)
	new_path += '/'
	x = 1

	for i in range(len(img_list)):
		img = img_list[i]
		author = img.get('alt')
		t1 = author.decode('gbk', 'ignore').encode('utf-8')
		link = img.get('data-src')
		print "It's downloading %s" %x + "th's piture"
		try:
		    urllib.urlretrieve(link, new_path + '%s.jpg' %author)
		except:
		    pass
		x += 1

