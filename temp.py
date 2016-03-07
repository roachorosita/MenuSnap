from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput

import json
import urllib2

class APICall:
    def __init__(self, longitude = 34.0295914, latitude = -117.414511, radius = 5000):
        self.lon = longitude
        self.lat = latitude
        self.rad = radius

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
import json
import urllib2


def locu_search(gps):
    #locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=34.056286,-117.81601&radius=1600&category=restaurant'

    def locu_search(self):
        print self.lon, self.lat

        #locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
        url = 'https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=' \
              + str(self.lon) + ',' + str(self.lat) + '&radius=' + str(self.rad) + '&category=restaurant'

        param = '{ "api_key" : "77ca60baa8056bc0c1aa6f422bc525a56ed1443e",' \
               ' "fields" : [ "name", "location", "contact", "website_url", "menu_url"],' \
               ' "venue_queries" : [{ "categories" : "restaurant",' \
               ' "location" : { "geo" : { "$in_lat_lng_radius" : [' + str(self.lon) + ', ' + str(self.lat) + ', ' + str(self.rad) + ']}}}]}'
        print param
        save = urllib2.urlopen('https://api.locu.com/v2/venue/search', data=param)
        result = json.load(save)
        print result
        return result

    def parse(self):

        data = self.locu_search()

        test = {'name': None, 'phone': None, 'url': None, 'menu_url': None, 'location': None, 'address': None}

        restaurant_list = []

        for item in range(5):
            restaurant_list.append(dict.copy(test))
            restaurant_list[item]['name'] = str(data['venues'][item]['name'])
            try: restaurant_list[item]['phone'] = str(data['venues'][item]['contact']['phone'])
            except: pass
            try: restaurant_list[item]['url'] = str(data['venues'][item]['website_url'])
            except: pass
            try: restaurant_list[item]['menu_url'] = str(data['venues'][item]['menu_url'])
            except: pass
            try: restaurant_list[item]['location'] = str(data['venues'][item]['location']['locality'])
            except: pass
            try: restaurant_list[item]['address'] = str(data['venues'][item]['location']['address1']) + \
                                               ' ' + str(data['venues'][item]['location']['locality']) + \
                                               ', ' + str(data['venues'][item]['location']['region']) + \
                                               ' ' + str(data['venues'][item]['location']['postal_code'])
            except: pass

        print self.lon, self.lat
        print 'parsing successful'
        print restaurant_list
        return restaurant_list

	
class HomeScreen(Screen):
    lon_value =  StringProperty()
    lat_value =  StringProperty()

    def update(self):
        self.ids.b1.text = MainApp.h[0]['name']
        self.ids.b2.text = MainApp.h[1]['name']
        self.ids.b3.text = MainApp.h[2]['name']
        self.ids.b4.text = MainApp.h[3]['name']
        self.ids.b5.text = MainApp.h[4]['name']
    pass
class Screen1(Screen):
    pass
class Screen2(Screen):
    pass
class Screen3(Screen):
    pass
class Screen4(Screen):
    pass
class Screen5(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        self.API = APICall()
        self.h = self.API.parse()
        return Builder.load_file("temp.kv")

if __name__ == '__main__':
    MainApp().run()
                       
