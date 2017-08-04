import os
import googlemaps
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



api_key = 'AIzaSyCvVC17BL_hM7MGOK7CMPZMba2i1iH7eus'

gm = googlemaps.Client(key = api_key)

folder = '/home/t28/Documents/ve450/final_demo_users/'
List = os.listdir(folder)
array_num = 0

for i in range(len(List)):
    author = List[i]
    array_num = array_num + 1
    print 'var markerArr' + str(array_num) + ' = [\n',

    new_folder = os.path.join(folder,author)
    new_list = os.listdir(new_folder)
    for j in range(len(new_list)):
        loc = new_list[j]
        loc = loc.split('_')[0]

        geocode_result = gm.geocode(loc)[0]

        name = geocode_result['formatted_address']

        location = geocode_result['geometry']['location']
        print'\t'+ '{' + 'title: '+  '"' + name.decode('utf-8') + '"' + ', point: ' + '"' + str(location['lng']) + ',' + str(location['lat']) + '"}',
        if j < (len(new_list) - 1):
            print ',\n',
        else:
            print '\n];\n',