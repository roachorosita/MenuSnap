import urllib2
import json

def locu_search(query):
    locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=34.056286,-117.81601&radius=1600&category=restaurant'

    param = '{ "api_key" : "77ca60baa8056bc0c1aa6f422bc525a56ed1443e",' \
           ' "fields" : [ "name", "location", "contact", "website_url", "menu_url"],' \
           ' "venue_queries" : [{ "categories" : "restaurant",' \
           ' "location" : { "geo" : { "$in_lat_lng_radius" : [34.0319273, -117.4165178, 5000]}}}]}'

    save = urllib2.urlopen('https://api.locu.com/v2/venue/search', data=param)
    result = json.load(save)

    for item in result['venues']:
        print item['name']
        try: print item['contact']['phone']
        except: pass
        try: print item['website_url']
        except: pass
        try: print item['menu_url']
        except: pass
        try: print item['location']['address1'] + ' ' + item['location']['locality'] + ' ' + item['location']['region'] + ' ' + item['location']['postal_code']
        except: pass
        print '\n'
    return result

data = locu_search('los angeles')
'''
#print data
test = {'name': None, 'phone': None, 'url': None, 'location': None, 'address': None}

restaurant_list = []

for i in range(5):
    restaurant_list.append(dict.copy(test))
    
for item in range(5):
    restaurant_list[item]['name'] = str(data['objects'][item]['name'])
    restaurant_list[item]['phone'] = str(data['objects'][item]['phone'])
    restaurant_list[item]['url'] = str(data['objects'][item]['website_url'])
    restaurant_list[item]['location'] = str(data['objects'][item]['locality'])
    restaurant_list[item]['address'] = str(data['objects'][item]['street_address']) + ' ' + str(data['objects'][item]['locality']) + ', ' + str(data['objects'][item]['region']) + ' ' + str(data['objects'][item]['postal_code']) 

print "Print the list: \n", restaurant_list
'''