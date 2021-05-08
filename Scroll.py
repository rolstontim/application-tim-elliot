import kivy
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from random import shuffle
from kivy.uix.gridlayout import GridLayout




class Scroll(ScrollView):


    #takes the filenames needed to access and the number of string needed
    #from each file and whatever kwargs Scrollview takes
    def __init__(self,filenames,n, **kwargs):
        super(Scroll,self).__init__(**kwargs)
        store = ''
        #might want to take multiple filenames for the different lengths
        for i,filename in enumerate(filenames):

            #open file
            f = open(filename,'r')
            #skip the first two lines

            f.readline()
            f.readline()
            #read all of the lines

            lst = f.readlines()
            #shuffle the lst, O(n) but lets me cut out one for loop
            shuffle(lst)

            #slice the necessary amount
            lst = lst[:n[i]]
            print(lst)
            #iterate through the remaining
            for string in lst:
                for index,char in enumerate(string):
                    if char == ',':
                        store += string[:index] + '\n'

            f.close()
        self.ids.lbl.text = store
        print(store)






class Myapp(App):
    def build(self):
        ret = GridLayout()
        ret.add_widget(Scroll(['motivators/short'],[20]))
        return ret




if __name__ == '__main__':
    Myapp().run()
