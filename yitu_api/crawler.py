#coding = 'utf-8'
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



    url = 'http://www.mafengwo.cn/u/sisisizi/note.html'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    author = soup.find_all('span',class_="MAvaName")[0]
    author = author.text
    article = soup.find_all('div',class_="note_info")
    _path = os.getcwd()
    new_path = os.path.join(_path , '%s' %(author))
    if not os.path.isdir(new_path):
        os.mkdir(new_path)

    for j in range(len(article)):

        new_url = article[j].find_all("a") #go to the specific blog
        if (len(new_url) == 1):
            new_url = new_url[0].get("href")
        else:
            new_url = new_url[1].get("href")

        new_url = "http://www.mafengwo.cn" + new_url
        res = requests.get(new_url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        imgs = soup.find_all("img")
        time = soup.find_all('li',class_="time")
        if time == []:
            time = 'unknown'
        else:
            time = time[0].text.split('/')[1]
        loc = soup.find_all('div',class_="relation_mdd opacity_on special_mdd")[0]
        loc = loc.a.get("title")
        #set up the folder
        new_path_j = os.path.join(new_path , '%s_%s' %(loc, time))
        if not os.path.isdir(new_path_j):
            os.mkdir(new_path_j)
        new_path_j += '/'

        x = 1
        if imgs == []:
            print "Done!"
        for img in imgs:
            link = img.get('data-rt-src')
            if link and "http" in link:
                print "It's downloading %s" %x + "th's piture"
                #link = 'http:' + link

                try:
                    urllib.urlretrieve(link, new_path_j + '%s.jpg' %x)
                except:
                    pass
                x += 1






