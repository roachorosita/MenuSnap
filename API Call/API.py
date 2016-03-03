import urllib
import urllib2
import json
import copy

def locu_search(query):
    locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=34.056286,-117.81601&radius=1600&category=restaurant'
    #url2 = 'https://api.locu.com/v1_0/menu_item/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&name=burrito'

    '''
    #limit = '&limit=5'
    city = query.replace(' ', '%20')
    #url = url + '&locality=' + city
    #name = query.replace(' ', '%20')
    final_url = url

    print final_url
    '''

    #json_obj2 = urllib2.urlopen(url2)
    #data2 = json.load(json_obj2)

    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    print data
    for item in data['objects']:
        print item['name']
        print item['phone']
        print item['website_url']
        print item['street_address']
        print item['postal_code']

    return data

data = locu_search('los angeles')
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
