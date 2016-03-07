from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
import json
import urllib2
kv = '''
# File name: temp.py
#: import FadeTransition kivy.uix.screenmanager.FadeTransition

ScreenManagement:
    transition: FadeTransition()
    HomeScreen:
    Screen1:
    Screen2:
    Screen3:
    Screen4:
    Screen5:

<HomeScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
		canvas.before:
			Color:
				rgba: 0, 0.5, 1, 0.5
			Rectangle:
				#self here refers to the widget--> BoxLayout
				pos: self.pos
				size: self.size
        Button:
            id: b1
			background_color: 0, 0, 1, 1
            on_release: root.manager.current = 'Screen1'
            text: app.h[0]['name']
            size_hint: 0.5, 0.15
            pos_hint: {'center_x': .5}
            font_size: 25
        Button:
            id: b2
			background_color: 0, 0, 1, 1
            on_release: root.manager.current = 'Screen2'
            text: app.h[1]['name']
            size_hint: 0.5, 0.15
            pos_hint: {'center_x': .5}
            font_size: 25
        Button:
            id: b3
			background_color: 0, 0, 1, 1
            on_release: root.manager.current = 'Screen3'
            text: app.h[2]['name']
            size_hint: 0.5, 0.15
            pos_hint: {'center_x': .5}
            font_size: 25
        Button:
            id: b4
			background_color: 0, 0, 1, 1
            on_release: root.manager.current = 'Screen4'
            text: app.h[3]['name']
            size_hint: 0.5, 0.15
            pos_hint: {'center_x': .5}
            font_size: 25
        Button:
            id: b5
			background_color: 0, 0, 1, 1
            on_release: root.manager.current = 'Screen5'
            text: app.h[4]['name']
            size_hint: 0.5, 0.15
            pos_hint: {'center_x': .5}
            font_size: 25
        GridLayout:
            size_hint: 0.5, 0.1
            pos_hint: {'center_x': 0.5}
            rows:1

            TextInput:
                name: 'latitude'
                hint_text: "Latitude"
                multiline: False
                on_text_validate:
                    app.API.lat =  self.text

            TextInput:
                name: 'longitude'
                hint_text: "Longitude"
                multiline: False
                on_text_validate:
                    app.API.lon =  self.text




            Button:
                text: "Refresh"
				background_color: 0, 0, 1, 1
                on_release:
                    app.h = app.API.parse()
                    root.ids.b1.text = app.h[0]['name']
                    root.ids.b2.text = app.h[1]['name']
                    root.ids.b3.text = app.h[2]['name']
                    root.ids.b4.text = app.h[3]['name']
                    root.ids.b5.text = app.h[4]['name']


<Screen1>:
    name: 'Screen1'
    BoxLayout:
        orientation: 'vertical'
		canvas.before:
			Color:
				rgba: 0, 0.5, 1, 0.5
			Rectangle:
				#self here refers to the widget--> BoxLayout
				pos: self.pos
				size: self.size
		Button:
			text: 'MENU'
			background_color: 0, 0, 1, 1
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[0]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
		    item_strings: [str("\nRESTAURANT"), str(app.h[0]['name']), str("\nPHONE NUMBER"), str(app.h[0]['phone']), str("\nWEBSITE"), str(app.h[0]['url']), str("\nADDRESS"), str(app.h[0]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'HOME'
			background_color: 0, 0, 1, 1
            font_size: 25
            pos_hint:{'center_x': 0.5, 'bottom':0}
            size_hint: 0.3, 0.1


<Screen2>:
    name: 'Screen2'
    BoxLayout:
        orientation: 'vertical'
		canvas.before:
			Color:
				rgba: 0, 0.5, 1, 0.5
			Rectangle:
				#self here refers to the widget--> BoxLayout
				pos: self.pos
				size: self.size
		Button:
			text: 'MENU'
			background_color: 0, 0, 1, 1
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[1]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
		    item_strings: [str("\nRESTAURANT"), str(app.h[1]['name']), str("\nPHONE NUMBER"), str(app.h[1]['phone']), str("\nWEBSITE"), str(app.h[1]['url']), str("\nADDRESS"), str(app.h[1]['address'])]

		Button:
            on_release: root.manager.current = 'main'
            text: 'HOME'
			background_color: 0, 0, 1, 1
            font_size: 25
            pos_hint:{'center_x': 0.5, 'bottom':0}
            size_hint: 0.3, 0.1

<Screen3>:
    name: 'Screen3'
    BoxLayout:
        orientation: 'vertical'
		canvas.before:
			Color:
				rgba: 0, 0.5, 1, 0.5
			Rectangle:
				#self here refers to the widget--> BoxLayout
				pos: self.pos
				size: self.size
		Button:
			text: 'MENU'
			background_color: 0, 0, 1, 1
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[2]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
            item_strings: [str("\nRESTAURANT"), str(app.h[2]['name']), str("\nPHONE NUMBER"), str(app.h[2]['phone']), str("\nWEBSITE"), str(app.h[2]['url']), str("\nADDRESS"), str(app.h[2]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'HOME'
			background_color: 0, 0, 1, 1
            font_size: 25
            pos_hint:{'center_x':0.5, 'bottom':0}
            size_hint: 0.3, 0.1


<Screen4>:
    name: 'Screen4'
    BoxLayout:
        orientation: 'vertical'
		canvas.before:
			Color:
				rgba: 0, 0.5, 1, 0.5
			Rectangle:
				#self here refers to the widget--> BoxLayout
				pos: self.pos
				size: self.size
		Button:
			text: 'MENU'
			background_color: 0, 0, 1, 1
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[3]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
            item_strings: [str("\nRESTAURANT"), str(app.h[3]['name']), str("\nPHONE NUMBER"), str(app.h[3]['phone']), str("\nWEBSITE"), str(app.h[3]['url']), str("\nADDRESS"), str(app.h[3]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'HOME'
			background_color: 0, 0, 1, 1
            font_size: 25
            pos_hint:{'center_x': 0.5, 'bottom':0}
            size_hint: 0.3, 0.1


<Screen5>:
    name: 'Screen5'
    BoxLayout:
        orientation: 'vertical'
		canvas.before:
			Color:
				rgba: 0, 0.5, 1, 0.5
			Rectangle:
				#self here refers to the widget--> BoxLayout
				pos: self.pos
				size: self.size
		Button:
			text: 'MENU'
			background_color: 0, 0, 1, 1
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[4]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
            item_strings: [str("\nRESTAURANT"), str(app.h[4]['name']), str("\nPHONE NUMBER"), str(app.h[4]['phone']), str("\nWEBSITE"), str(app.h[4]['url']), str("\nADDRESS"), str(app.h[4]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'HOME'
			background_color: 0, 0, 1, 1
            font_size: 25
            pos_hint:{'center_x':0.5, 'bottom':0}
            size_hint: 0.3, 0.1
'''

class APICall:
    def __init__(self, longitude = -117.4145, latitude = 34.02959, radius = 5000):
        self.lon = longitude
        self.lat = latitude
        self.rad = radius
      
	#Modify latitude and longitude once the user enters the new values	
    def locu_search(self):

        #locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
        url = 'https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=' \
              + str(self.lat) + ',' + str(self.lon) + '&radius=' + str(self.rad) + '&category=restaurant'

        param = '{ "api_key" : "77ca60baa8056bc0c1aa6f422bc525a56ed1443e",' \
               ' "fields" : [ "name", "location", "contact", "website_url", "menu_url"],' \
               ' "venue_queries" : [{ "categories" : "restaurant",' \
               ' "location" : { "geo" : { "$in_lat_lng_radius" : [' + str(self.lat) + ', ' + str(self.lon) + ', ' + str(self.rad) + ']}}}]}'
        save = urllib2.urlopen('https://api.locu.com/v2/venue/search', data=param)
        result = json.load(save)
        return result
		
		
	#retrieving data from locu API
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
        return restaurant_list

#defining the main
class HomeScreen(Screen):
    lon_value =  StringProperty()
    lat_value =  StringProperty()
    
	#update the names of each button on the home screen
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

#main	
class MainApp(App):

    def build(self):
        self.API = APICall()
        self.h = self.API.parse()
        return Builder.load_file("temp.kv")

if __name__ == '__main__':
    MainApp().run()
                       
