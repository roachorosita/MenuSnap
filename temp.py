from kivy.app import App
#kivy.require("1.9.2")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

import json
import urllib2

def locu_search(gps):
    #locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=34.056286,-117.81601&radius=1600&category=restaurant'

    param = '{ "api_key" : "77ca60baa8056bc0c1aa6f422bc525a56ed1443e",' \
           ' "fields" : [ "name", "location", "contact", "website_url", "menu_url"],' \
           ' "venue_queries" : [{ "categories" : "restaurant",' \
           ' "location" : { "geo" : { "$in_lat_lng_radius" : [34.0319273, -117.4165178, 5000]}}}]}'

    save = urllib2.urlopen('https://api.locu.com/v2/venue/search', data=param)
    result = json.load(save)
    return result

def parse():

    data = locu_search('test')

    test = {'name': None, 'phone': None, 'url': None, 'menu_url': None, 'location': None, 'address': None}

    restaurant_list = []

    for item in range(5):
        print "swag"
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

    return restaurant_list

class HomeScreen(Screen):
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

    h=parse()
    print h
    def build(self):
        return Builder.load_file("temp.kv")

if __name__ == '__main__':
    MainApp().run()
                       
