from kivy.lang import Builder
from plyer import gps
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout

import json
import urllib2

kv = '''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import ListAdapter kivy.adapters.listadapter.ListAdapter

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
        size_hint_y: None
        height: '48dp'
        padding: '4dp'

        ToggleButton:
            text: 'Start' if self.state == 'normal' else 'Stop'
            on_state:
                app.gps.start() if self.state == 'down' else app.gps.stop()
    Button:
        on_release: root.manager.current = 'Screen1'
        text: app.h[0]['name']
        size_hint:self.parent.width, 0.15
        pos_hint:{'center_x': .5, 'center_y': .80}
        font_size: 25
    Button:
        on_release: root.manager.current = 'Screen2'
        text: app.h[1]['name']
        size_hint: self.parent.width, 0.15
        pos_hint:{'center_x': .5, 'center_y': .65}
        font_size: 25
    Button:
        on_release: root.manager.current = 'Screen3'
        text: app.API[2]['name']
        size_hint:self.parent.width, 0.15
        pos_hint:{'center_x': .5, 'center_y': .5}
        font_size: 25
    Button:
        on_release: root.manager.current = 'Screen4'
        text: app.h[3]['name']
        size_hint:self.parent.width, 0.15
        pos_hint:{'center_x': .5, 'center_y': .35}
        font_size: 25
    Button:
        on_release: root.manager.current = 'Screen5'
        text: app.h[4]['name']
        size_hint:self.parent.width, 0.15
        pos_hint:{'center_x': .5, 'center_y': .2}
        font_size: 25
    Button:
        on_release:
        text: app.h[4]['name']
        size_hint:self.parent.width, 0.15
        pos_hint:{'center_x': .5, 'center_y': .2}
        font_size: 25
    GridLayout:
        size_hint: self.parent.width, 0.15
        pos_hint:{'center_x': .5, 'center_y': 0.05}
        rows:2
        Label:
            text: app.gps_status
        Label:
            text: "Current Location"
            font_size: 15
            valign: 'bottom'
            halign: 'center'

<Screen1>:
    name: 'Screen1'
    BoxLayout:
        orientation: 'vertical'
		Button:
			text: 'menu'
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[0]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
		    font_size: 25
            item_strings: [str(app.h[0]['name']), str(app.h[0]['phone']), str(app.h[0]['url']), str(app.h[0]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'Home'
            font_size: 25
            pos_hint:{'left':0, 'bottom':0}
            size_hint: 0.3, 0.1

<Screen2>:
    name: 'Screen2'
    BoxLayout:
        orientation: 'vertical'
		Button:
			text: 'menu'
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[1]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
		    font_size: 25
            item_strings: [str(app.h[1]['name']), str(app.h[1]['phone']), str(app.h[1]['url']), str(app.h[1]['address'])]

		Button:
            on_release: root.manager.current = 'main'
            text: 'Home'
            font_size: 25
            pos_hint:{'left':0, 'bottom':0}
            size_hint: 0.3, 0.1

<Screen3>:
    name: 'Screen3'
    BoxLayout:
        orientation: 'vertical'
		Button:
			text: 'menu'
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[2]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
		    font_size: 25
            item_strings: [str(app.h[2]['name']), str(app.h[2]['phone']), str(app.h[2]['url']), str(app.h[2]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'Home'
            font_size: 25
            pos_hint:{'left':0, 'bottom':0}
            size_hint: 0.3, 0.1

<Screen4>:
    name: 'Screen4'
    BoxLayout:
        orientation: 'vertical'
		Button:
			text: 'menu'
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[3]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
		    font_size: 25
            item_strings: [str(app.h[3]['name']), str(app.h[3]['phone']), str(app.h[3]['url']), str(app.h[3]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'Home'
            font_size: 25
            pos_hint:{'left':0, 'bottom':0}
            size_hint: 0.3, 0.1


<Screen5>:
    name: 'Screen5'
    BoxLayout:
        orientation: 'vertical'
		Button:
			text: 'menu'
		    on_release:
			    import webbrowser
				webbrowser.open(str(app.h[4]['menu_url']))
			font_size: 20
			pos_hint:{'center_x': 0.5, 'center_y': 0}
			size_hint: 0.3, 0.1

		ListView:
		    font_size: 25
            item_strings: [str(app.h[4]['name']), str(app.h[4]['phone']), str(app.h[4]['url']), str(app.h[4]['address'])]


		Button:
            on_release: root.manager.current = 'main'
            text: 'Home'
            font_size: 25
            pos_hint:{'left':0, 'bottom':0}
            size_hint: 0.3, 0.1
'''

class APICall:
    def __init__(self,lon,lat):
        self.lon = 0
        self.lat = 0

    def locu_search(self):
        #locu_api = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'
        url = 'https://api.locu.com/v1_0/venue/search/?api_key=77ca60baa8056bc0c1aa6f422bc525a56ed1443e&location=' + self.lon + ',' + self.lat + '&radius=1600&category=restaurant'

        param = '{ "api_key" : "77ca60baa8056bc0c1aa6f422bc525a56ed1443e",' \
               ' "fields" : [ "name", "location", "contact", "website_url", "menu_url"],' \
               ' "venue_queries" : [{ "categories" : "restaurant",' \
               ' "location" : { "geo" : { "$in_lat_lng_radius" : [34.0319273, -117.4165178, 5000]}}}]}'

        save = urllib2.urlopen('https://api.locu.com/v2/venue/search', data=param)
        result = json.load(save)
        return result

    def parse(self):

        data = self.locu_search('test')

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

        return restaurant_list()

def mainthread(func):
    # This method is now part of Kivy 1.8.0. When it's released, remove it.
    def delayed_func(*args, **kwargs):
        def callback_func(dt):
            func(*args, **kwargs)
        Clock.schedule_once(callback_func, 0)
    return delayed_func

class GpsTest(App):

    gps_location = StringProperty()
    gps_status = StringProperty('Click Start to get GPS location updates')
    gps_lon = 0
    gps_lat = 0
    API = APICall(0,0)
    h = {}

    def build(self):
        self.gps = gps
        try:
            self.gps.configure(on_location=self.on_location,
                    on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'

        return Builder.load_string(kv)

    @mainthread
    def on_location(self, **kwargs):
        self.API.lon = '{lon}'.format(**kwargs)
        self.API.lat = '{lat}'.format(**kwargs)
        h = self.API.parse()

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'gps type={}\n{}'.format(stype, status)

if __name__ == '__main__':
    GpsTest().run()
