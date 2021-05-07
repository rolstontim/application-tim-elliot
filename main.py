import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,  Screen, CardTransition
from kivy.lang import Builder


class HomeScreen(Screen):


#code for detecting upward swipe on bottom of screen - if so then change to stat_screen

    def on_touch_move(self, touch):
        if touch.y < self.height/4:

            if touch.dy > 0.03*self.height:

                TimeShamer.get_running_app().change_screen("stat_screen")


    def on_touch_up(self,touch):
        if touch.oy < self.height*(1/4):

            if touch.y > self.height*1/3:

                TimeShamer.get_running_app().change_screen("home_screen")




class StatScreen(Screen):


#to detect downward swipe on top of screen - if so then change to home_screen
    def on_touch_move(self, touch):

        if touch.oy > self.height*(3/4):




            if touch.dy < -0.03*self.height:
                TimeShamer.get_running_app().change_screen("home_screen")

    def on_touch_up(self,touch):



        if touch.oy > self.height*(3/4):

            if touch.y < self.height*2/3:

                TimeShamer.get_running_app().change_screen("home_screen")

#class WindowManager(ScreenManager):
#   pass



kv = Builder.load_file("TimeShamer.kv")

class TimeShamer(App):
    def build(self):
        #defined at bottom - for kv file
        return GUI


    def change_screen(self, screen_name):

        screen_manager = self.root.ids["screen_manager"]

        #screen_manager.current = screen_name

        #transitions for home to stat screen
        if screen_name == "stat_screen":
            print("in here")
            screen_manager.transition = CardTransition(direction = "up")
            #screen_manager.current = screen_name

        #transitions for stat to home screen
        if screen_name == "home_screen":
            #print("in here")
            screen_manager.transition = CardTransition(direction = "down", mode = "pop")
            #screen_manager.current = screen_name

        screen_manager.current = screen_name


    def quit_app(self):
        TimeShamer().stop()

GUI = Builder.load_file("TimeShamer.kv")

if __name__ == '__main__':
    TimeShamer().run()
