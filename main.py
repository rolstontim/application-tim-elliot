import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,  Screen, CardTransition
from kivy.lang import Builder
<<<<<<< HEAD
from Scroll import Scroll
=======

from scroll import Scroll
import random

>>>>>>> 5f97d9ffe1ff2870700b156f2e11792903efaa6c

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





class TimeShamer(App):
    def build(self):
        #defined at bottom - for kv file
        return GUI


#Code to read stats into files


    def on_start(self):


        #stat_list =  self.root.ids["stat_screen"].ids["stat_list"]

        #create scroll page
        self.read_stats("example_android_data/battery_usage")





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



#Code to read stats into files
    def read_stats(self, filename):
        #declare where the stat_list is located
        stat_list =  self.root.ids["stat_screen"].ids["stat_list"]
        #motivators (minutes)
        mot_short = 0
        mot_medium = 60
        mot_long = 1440
        mot_life_impacting = 43800
        category = "short"
        minute_multiplyer = 1

        #Populate list of applications and their usage (time) in minutes
        with open(filename) as fp:
            app_lines = fp.readlines()

        for app_line in app_lines:

            #get name of app
            app_name = app_line[:app_line.find(",")]
            print("APP NAME: ", app_name)

            #get time used of append
            app_time = int(app_line[app_line.find(",") + 1:app_line.find('\n')])
            print("APP TIME: ", app_time)

            #determine motivator category
            if (mot_short < app_time and app_time < mot_medium):
                category = "short"
                minute_multiplyer = 1
            elif (mot_medium <= app_time and app_time < mot_long):
                category = "medium"
                minute_multiplyer = 60
            elif (mot_long <= app_time and app_time < mot_life_impacting):
                category = "long"
                minute_multiplyer = 1440
            else:
                category = "life_impacting"
                minute_multiplyer = 43800


            #go into correct category and populate new list with motivators within app_time range
            with open("motivators/" + category) as f:
                next(f)
                motivators = f.readlines()
            i = 0
            #remove motivators that are out of range of app_time (ie motivator time > app_time via minutes)
            for motivator_line in motivators:

                if (int(motivator_line[motivator_line.find(",") + 1:motivator_line.find('\n')]) * minute_multiplyer > app_time):
                    del motivators[i]
                i += 1

            #pick random motivator from motivators to represent
            motivator = random.choice(motivators)

            #get name of random motivator
            motivator_name = motivator[:motivator.find(",")]

            #get recalulated time of random motivator (based on app_time)
            time_spent = int(motivator[motivator.find(",") + 1:motivator.find('\n')]) * minute_multiplyer
            time_spent = app_time/time_spent

            #call scroll function to display widget of app stat in stat screen
            s = Scroll(app_name,motivator_name)
            #put wrapped widget from Scroll class into stat_screen for display
            stat_list.add_widget(s)



    def quit_app(self):
        TimeShamer().stop()

GUI = Builder.load_file("TimeShamer.kv")

if __name__ == '__main__':
    TimeShamer().run()
