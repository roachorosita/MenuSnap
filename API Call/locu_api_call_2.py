import urllib2
import json

def locu_search(city):
    '''
    locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
    url = 'https://api.locu.com/v2/venue/search/?locality='
    #limit = '&limit=5'
    city.replace(' ', '%20')
    url = url + city + '&api_key=' + locu_api
'''
    url = 'https://api.locu.com/v2/venue/search/'
    request = requests.get(url)

    print request
'''
    for item in data['objects']:
        print item
'''
locu_search('los angeles')