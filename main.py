import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,  Screen
from kivy.lang import Builder

class Window1(Screen):
    pass


class Window2(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('TimeShamer.kv')

class TimeShamer(App):
    def build(self):
        return kv



if __name__ == '__main__':
    TimeShamer().run()
