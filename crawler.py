#coding = 'utf-8'
import requests
from bs4 import BeautifulSoup
import urllib
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':


    for i in range(1): #number of pages of travel blog

        url = 'http://360.mafengwo.cn/travels/'
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        t2 = soup.find_all('div',class_="itemBd")
        for j in range(len(t2)):

            new_url = t2[j].a.get('href') #go to the specific blog
            new_url = "http://360.mafengwo.cn" + new_url
            res = requests.get(new_url)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text, 'html.parser')
            imgs = soup.find_all("img")
            loc = soup.find_all('div',class_="crumb")[0]
            loc = loc.find_all("a")[1].text
            author = soup.find_all('div',class_="author")[0]
            author = author.p.text
            author = author.split()[0]
            _path = os.getcwd()
            #set up the folder
            new_path = os.path.join(_path , '%s_%s' %(author, loc))
            if not os.path.isdir(new_path):
                os.mkdir(new_path)
            new_path += '/'

            x = 1
            if imgs == []:
                print "Done!"
            for img in imgs:
                link = img.get('src')
                if "http" in link:
                    print "It's downloading %s" %x + "th's piture"
                    #link = 'http:' + link
                    urllib.urlretrieve(link, new_path + '%s.jpg' %x)
                    x += 1






