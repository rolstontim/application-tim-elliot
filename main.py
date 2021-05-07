import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,  Screen, CardTransition
from kivy.lang import Builder



class HomeScreen(Screen):

    #apparently there is a carousel function that might be worth looking into
    #instead of doing it like this
    def on_touch_move(self,touch):
        if touch.y < self .height/4:
            TimeShamer.get_running_app().change_screen('Window2')



class Window2(Screen):

    def on_touch_move(self,touch):
        if touch.y > self.height*3/4:
            TimeShamer.get_running_app().change_screen('HomeScreen')
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('TimeShamer.kv')

class TimeShamer(App):
    def build(self):
        return kv


    def change_screen(self, screen_name):

        #the way I implemented the kv file the root is the screen manager idk
        #if this is the best way to implement it
        screen_manager = self.root


        if screen_name == 'Window2':
            screen_manager.transition = CardTransition(direction = 'up')


        else:
            screen_manager.transition = CardTransition(direction = 'down', mode = 'pop')


        screen_manager.current = screen_name


    def quit_app(self):
        TimeShamer().stop()


if __name__ == '__main__':
    TimeShamer().run()
