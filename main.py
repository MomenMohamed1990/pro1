from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput



class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs)
        self.cols=2
        self.set_center_x=True
        #self.set_center_y=True
        #self.size=(400,400)
        self.row_force_default=True
        self.row_default_height=150
        self.col_force_default=True
        self.col_default_width=200  
        self.l1 = Label(text = "First number")
        self.add_widget(self.l1)
        self.txin1 = TextInput(multiline=True)
        self.add_widget(self.txin1)
        self.l2 = Label(text = "Second number")
        self.add_widget(self.l2)
        self.txin2 = TextInput(multiline=True)
        self.add_widget(self.txin2)
        self.l3 = Label(text = "Result")
        self.add_widget(self.l3)
        self.txin3 = TextInput(multiline=True)
        self.add_widget(self.txin3)
        self.new_widget=GridLayout()
        self.add_widget(self.new_widget)
        self.new_widget.cols=4
        self.new_widget.row_force_default=True
        self.new_widget.row_default_height=100
        self.new_widget.col_force_default=True
        self.new_widget.col_default_width=100   
        

        self.btn1 = Button(text = "Add")
        self.btn1.bind(on_press=self.add)
        self.new_widget.add_widget(self.btn1)
        self.btn2 = Button(text = "Subtract")
        self.btn2.bind(on_press=self.sub)
        self.new_widget.add_widget(self.btn2)   
        self.btn3 = Button(text = "Multiply")
        self.btn3.bind(on_press=self.mul)
        self.new_widget.add_widget(self.btn3)
        self.btn4 = Button(text = "Divide")
        self.btn4.bind(on_press=self.div)
        self.new_widget.add_widget(self.btn4)   
    def add(self,instance):
        x = self.txin1.text
        y = self.txin2.text
        self.txin3.text = str(int(x)+int(y))
        return int(x)+int(y)
    def sub(self,instance):
        x = self.txin1.text
        y = self.txin2.text
        self.txin3.text = str(int(x)-int(y))
        return int(x)-int(y)
    def mul(self,instance):
        x = self.txin1.text
        y = self.txin2.text 
        self.txin3.text = str(int(x)*int(y))
        return int(x)*int(y)
    def div(self,instance):
        x = self.txin1.text
        y = self.txin2.text 
        self.txin3.text = str(int(x)/int(y))
        return int(x)/int(y)


class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ == '__main__':
    MyApp().run()        