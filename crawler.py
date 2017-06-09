#coding = 'utf-8'
import requests
from bs4 import BeautifulSoup
import urllib
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    imgs = [];
    for i in range(5):
        #url = 'https://www.qiushibaike.com/imgrank/
        url = 'http://www.dbmeinv.com/dbgroup/show.htm?cid=2'
        url = url + '&pager_offset=%s' %i
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        imgs_i = soup.find_all("img")
        imgs.extend(imgs_i)

    _path = os.getcwd()
    new_path = os.path.join(_path , 'try1_photos')
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    new_path += '\ '

    x = 1
    if imgs == []:
        print "Done!"
    for img in imgs:
        link = img.get('src')
        print "It's downloading %s" %x + "th's piture"
        #link = 'http:' + link
        urllib.urlretrieve(link, new_path + '%s.jpg' %x)
        x += 1






