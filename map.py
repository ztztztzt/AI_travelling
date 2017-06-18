coding = 'utf-8'
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import cv2
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import pandas as pd
city = pd.read_excel("citylist.xlsx")
city[u'城市中文名']
shanghai = city[city[u'城市中文名'].isin([u'上海'])]
jingdu = city[city[u'城市中文名'].isin([u'京都'])]
lat_s = str(shanghai[u'纬度']).split()[1]
lat_s = re.findall(r'(\w*[0-9]+)\w*',lat_s) #get the number
lat_s = float(lat_s[0] + '.' + lat_s[1])

lon_s = str(shanghai[u'经度']).split()[1]
lon_s = re.findall(r'(\w*[0-9]+)\w*',lon_s) #get the number
lon_s = float(lon_s[0] + '.' + lon_s[1])

lat_j = str(jingdu[u'纬度']).split()[1]
lat_j = re.findall(r'(\w*[0-9]+)\w*',lat_j) #get the number
lat_j = float(lat_j[0])

lon_j = str(jingdu[u'经度']).split()[1]
lon_j = re.findall(r'(\w*[0-9]+)\w*',lon_j) #get the number
lon_j = float(lon_j[0] + '.' + lon_j[1])



img = plt.imread('2.png', format='jpeg')

cv2.destroyAllWindows()


m = Basemap(projection ='mill',
            llcrnrlon = -180, llcrnrlat = -55,
            urcrnrlon = 180, urcrnrlat = 85)

m.drawcoastlines()
m.fillcontinents()
m.drawcountries()
m.drawgreatcircle(lon_s,lat_s,lon_j,lat_j,linewidth=2,color='b')

x,y = m(lon_s, lat_s)
im = OffsetImage(img, zoom=0.3)
ab = AnnotationBbox(im, (x,y), xycoords='data', frameon=False)

m._check_ax().add_artist(ab)

plt.show()