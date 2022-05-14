from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window

from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase


# class MyScreenManager(ScreenManager):
#     total_button = NumericProperty(2)
# def submit():
#     sm.current='select'
inde = None
indee = None
db = DataBase('machines.json')
db.load()


class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

        self.count = 0
        #The default is"horizontal"It is placed horizontally.
        self.orientation = "horizontal"
        #self.orientation = "vertical"

        btn = Button(text='Hello World', on_release=self.submit)
        self.add_widget(btn)
    def submit(self):
        sm.current='select'

    def click(self,btn):
        self.count += 1
        self.add_widget(Button(text="{}".format(self.count),on_press=self.dismiss))

    def dismiss(self, a):
        self.remove_widget(a)
class MachineWindow(Screen):

    # container = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(MachineWindow, self).__init__(**kwargs)
        # self.container = Test()
   # contaier = Test()

        # self.count = 0
        # #The default is"horizontal"It is placed horizontally.
        # self.orientation = "horizontal"
        # #self.orientation = "vertical"
        # for i in range(2):
        #     btn = Button(text='Hello World')
        #     self.add_widget(btn)


    def on_pre_enter(self):
        Window.maximize()

    def add_buttons(self):
        global indee,inde
        mache = db.machines
        counter=0
        for k,v in mache.items():
            # print(ind,i)
            # self.ids[ind]="Μηχάνημα #{}".format(ind)
            btn = Button(text="{}".format(k),on_release= self.switch,size_hint=(.1, .1),pos_hint={'x':.1, 'y':0.9 - counter*0.25})
            counter=counter+1
            # btn.bind(on_release=self.callback)
            self.add_widget(btn)
    # names = ['one','two','three']
    # for ind in range(3):
    #         container.add_widget(Button(text='machine #{}'.format(ind),on_release=submit()))

    # @staticmethod

    def switch(self,*args,**kwargs):
        global indee,inde
        # print(self.ids)
        # print(args[0].__dict__['_label'].__dict__)
        # print(kwargs)
        indee = args[0].__dict__['_label'].__dict__['_text']
        # print(indee)
        sm.current = 'select'
    def add_machine(self):
        sm.current='machine_add'

    # @staticmethod
    # def callback(*args, **kwargs):
    #     print(args[1].__dict__, kwargs)



    # def callback(instance):
    #     print('My button <%s> state is <%s>' % (instance))





class AddMachine(Screen):
    def __init__(self, **kwargs):
        super(AddMachine, self).__init__(**kwargs)
    namee = ObjectProperty(None)

    def submit(self):

        db.add_machine(self.namee.text)
        sm.current = 'main'
    def login(self):
        # self.reset()
        sm.current = "main"

class AddPart(Screen):
    def __init__(self, **kwargs):
        super(AddPart, self).__init__(**kwargs)
    namee = ObjectProperty(None)

    def submit(self):

        db.add_part(indee,self.namee.text)
        sm.current = 'select'
    def login(self):
        # self.reset()
        sm.current = "select"



class PartWindow(Screen):



    def __init__(self, **kwargs):
        super(PartWindow, self).__init__(**kwargs)
        # self.container = Test()

    # contaier = Test()

    # self.count = 0
    # #The default is"horizontal"It is placed horizontally.
    # self.orientation = "horizontal"
    # #self.orientation = "vertical"
    # for i in range(2):
    #     btn = Button(text='Hello World')
    #     self.add_widget(btn)

    def on_enter(self):
        # Window.size = (640, 360)
        Window.maximize()
    def add_buttons(self):
        global indee,inde
        names = ['ένα', 'δύο', 'τρία']
        mache = db.machines
        counter=0
        print(indee)
        for k,v in mache[indee].items():
            print(k)
            # for k2,v2 in v.items():
            # print(ind,i)
            self.ids[counter] = "button #{}".format(counter)
            btn = Button(text="{}".format(k), on_release=self.switch, size_hint=(.1, .1),
                         pos_hint={'x': .1, 'y': 0.9 - counter * 0.25})
            counter=counter+1

            # btn.bind(on_release=self.callback)
            self.add_widget(btn)
        btn = Button(text="Προσθεστε εξάρτημα", on_release=self.add_part, size_hint=(.1, .1),font_size=15,
                     pos_hint={'x':0.85,'y':0.9})
        self.add_widget(btn)
        btn = Button(text="Πίσω", on_release=self.go_back, size_hint=(.2, .1),font_size=14,
                     pos_hint={'x': .8, 'y': 0.0})
        self.add_widget(btn)
    def switch(self,*args,**kwargs):
        global indee, inde
        # print(self.ids)
        # print(args[0].__dict__['_label'].__dict__)
        # print(kwargs)
        inde = args[0].__dict__['_label'].__dict__['_text']
        # print(inde)
        sm.current = 'Parts'

    def go_back(self,*args,**kwargs):
        # sm.clear_widgets(screens=('Parts'))
        sm.current = 'main'
    # @staticmethod
    def refresh(self):
        # for widget in self.walk():
        #     print("{} -> {}".format(widget, widget.ids))
        #     # print(widget.ids)
        #     print(self.ids)
        #     if widget.ids == self.ids:
        #         self.remove_widget(widget)
        self.clear_widgets()
        # btn = Button(text="Πίσω", on_release=self.go_back(), size_hint=(.1, .1),
        #              pos_hint={'x': .1, 'y': 0.9 - 0.25})

        # sm.remove_widget(src)
        # print('removed widgets')
        # sm.add_widget(PartInfo(name='Parts'))
    def add_part(self,*args,**kwargs):

        sm.current='part_add'


# def _load_info():
#     # global indee,inde
#     # self.name2 = db.machines[indee][inde]['name']
#     # self.last_main=  db.machines[indee][inde]['Last Maintenance']
#     # self.next_main = db.machines[indee][inde]['Next Maintenance']
#     # elf.comms = db.machines[indee][inde]['Comments']s
#     print('fuck you')


class PartInfo(Screen):
    def __init__(self, **kwargs):
        super(PartInfo, self).__init__(**kwargs)
    name2 = StringProperty('')
    last_main = StringProperty('')
    next_main = StringProperty('')
    comms = StringProperty('')

    def on_pre_enter(self):
        Window.maximize()

    def load_info(self):
        self.name2 = db.machines[indee][inde]['name']
        self.last_main = db.machines[indee][inde]['Last Maintenance']
        self.next_main = db.machines[indee][inde]['Next Maintenance']
        self.comms = db.machines[indee][inde]['Comments']



    def go_back(self):
        sm.current = 'select'


class MyMainApp(App):
    def build(self):
        return sm



class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my2.kv")
sm = WindowManager()
# db = DataBase("users.txt")

screens = [AddMachine(name='machine_add'), PartWindow(name='select'), MachineWindow(name='main'),PartInfo(name='Parts'),AddPart(name='part_add')]
for screen in screens:
    sm.add_widget(screen)
# print(sm.__dict__)
sm.current = 'main'
if __name__ == "__main__":
    MyMainApp().run()

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
