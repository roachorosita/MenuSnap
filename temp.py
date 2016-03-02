from kivy.app import App
#kivy.require("1.9.2")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout


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


screens = Builder.load_file("temp.kv")

class MainApp(App):
    def build(self):
        return screens
#ed
#if __name__ == '__main__':
MainApp().run()
                       
