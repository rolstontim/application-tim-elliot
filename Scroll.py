from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image



#Class to turn a series of labels into a widget that is scrollable
class Scroll(GridLayout):
    cols = 2

    def __init__(self, app_name, motivator_name, **kwargs):
        super(Scroll, self).__init__(**kwargs)

        #sizing for the labels and images for each row

        #app_image_layout = FloatLayout()
        #app_image = Image(source = "backgrounds/app_image.png", size_hint=(1, 0.8), pos_hint={"top": 1, "right": 1})


        #it may be better to use a GridLayout for a more dynamic allocation of labels

        stat_screen = FloatLayout()
        app_image = Image(source = "backgrounds/app_image.png", size_hint=(1.8, 0.8), pos_hint={"top": 1, "right": 1})
        app_label = Label(text=app_name, size_hint=(0.8, 0.8), pos_hint={"top": 1, "right": 1})
        app_label.bind(width=lambda *x: app_label.setter('text_size')(app_label, (app_label.width, None)))

        motivator_label = Label(text=motivator_name, size_hint=(0.5,0.8), pos_hint={"top": 1, "right": 1})
        motivator_label.bind(width=lambda *x: motivator_label.setter('text_size')(motivator_label, (motivator_label.width, None)))
        #to add labels into one widget
        stat_screen.add_widget(motivator_label)
        stat_screen.add_widget(app_label)
        stat_screen.add_widget(app_image)

        #wrap the widget for returning
        #self.add_widget(app_image_layout)
        self.add_widget(stat_screen)
