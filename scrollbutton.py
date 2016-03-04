from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.app import App
#kivy.require("1.9.2")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
'''
class HomeScreen(Screen):
    pass



class NewButton(Button):
    pass

class ScreenManagement(ScreenManager):
    pass
'''

class NewButton(Button):
    Button.font_size = 25
    Button.on_release = root.manager.current = "screen"

class NewScreen(Screen):
    name = "screen"
    sm.add_widget()
    pass

sm = ScreenManager()
'''
# Add few screens
for i in range(4):
    screen = Screen(name='Title %d' % i)
    sm.add_widget(screen)
'''
class Example(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(10):
            btn = Factory.NewButton(text=str(i), size_hint=(1, None))
            layout.add_widget(btn)
        root = ScrollView()
        root.add_widget(layout)
        return root

if __name__ == '__main__':
    Example().run()