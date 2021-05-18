from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image



#Class to turn a series of labels into a widget that is scrollable
class Scroll(GridLayout):
    rows = 1

    def __init__(self, app_name, motivator_name, **kwargs):
        super(Scroll, self).__init__(**kwargs)

        #sizing for the labels and images for each row
        stat_screen = FloatLayout()
        app_image = Image(source = "backgrounds/app_image.png", size_hint=(1.8, 0.8), pos_hint={"top": 1, "right": 1})
        app_label = Label(text=app_name, size_hint=(1.5, 0.8), pos_hint={"top": 1, "right": 1})
        motivator_label = Label(text=motivator_name, size_hint=(0.8,0.8), pos_hint={"top": 1, "right": 1})

        #to add labels into one widget
        stat_screen.add_widget(app_image)
        stat_screen.add_widget(app_label)
        stat_screen.add_widget(motivator_label)

        #wrap the widget for returning
        self.add_widget(stat_screen)
