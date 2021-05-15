import kivy
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from random import shuffle
from kivy.uix.gridlayout import GridLayout




class Scroll(ScrollView):

    #takes the filenames needed to access and the number of string needed
    #from each file and whatever kwargs Scrollview takes
    def __init__(self, **kwargs):
        super(Scroll,self).__init__(**kwargs)
        times = self.readtimes()
        n = self.get_n(times)
        self.make_scroll(n)



    def readtimes(self):
        #make an empty list to store the times
        times = []

        #open the file containing the desired data
        f = open('example_android_data/battery_usage')

        #read the first line
        line = f.readline()

        #loop until the file is read
        while  line != '':

            #empty string to store the time
            time = ''
            #make a flag
            start = False

            for char in line:



                #if we've passed the comma read in the data
                if start:
                    time += char

                #if we reach a comma raise the flag
                if char == ',':
                    start = True

            #append the time to the return
            times.append(int(time[:-1]))

            #read the next line
            line = f.readline()

        #close the file
        f.close()

        return times




    def get_n(self,times):

        n1 = [x for x in times if x >= 730.1]
        n2 = [x for x in times if x >= 24 and x < 730.1]
        n3 = [x for x in times if x >= 1 and x < 24]
        n4 = [x for x in times if x < 1]

        return [len(n1),len(n2),len(n3),len(n4)]

    def make_scroll(self,n,**kwargs):

        filenames = ['motivators/life_impacting','motivators/short',
                     'motivators/medium','motivators/long' ]

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
        return





class Myapp(App):
    def build(self):
        ret = GridLayout()
        ret.add_widget(Scroll())
        return ret




if __name__ == '__main__':
    Myapp().run()
