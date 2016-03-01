from kivy.app import App
#kivy.require("1.9.2")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
#from kivy.animation import Animation, AnimationTransition
#from kivy.uix.widget import Widget


class HomeScreen(Screen):
    pass
class OptionScreen(Screen):
    pass
class ScreenManagement(ScreenManager):
    pass
#class CustomLayout(FloatLayout):
    #pass
#class SmileAnimate(Animation):
    #pass

screens = Builder.load_file("temp.kv")

class MainApp(App):
    def build(self):
        return screens
#ed
#if __name__ == '__main__':
MainApp().run()
                       
