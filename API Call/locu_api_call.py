import urllib2
import json
url = urllib2.urlopen('https://api.locu.com/v1_0/venue/search/?name=starbucks&api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e')
print(json.load(url))
#locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'