import requests
import json
import urllib2

param = '{ "api_key" : "f165c0e560d0700288c2f70cf6b26e0c2de0348f",' \
       ' "fields" : [ "name", "location", "contact", "website_url", "menu_url"],' \
       ' "venue_queries" : [{ "categories" : "restaurant",' \
       ' "location" : { "geo" : { "$in_lat_lng_radius" : [34.0319273, -117.4165178, 5000]}}}]}'

save = urllib2.urlopen('https://api.locu.com/v2/venue/search', data=param)
result = json.load(save)
print result
