from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.core.window import Window


class Calculator(Widget):
    ans = StringProperty('0')

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.num = []
        self.history = 0
        self.operator = ''
        pass

    def AcButton(self):
        self.num = []
        self.ans = '0'
        self.history = 0
        self.operator = ''
    
    def CButton(self):
        self.num = []
        self.ans = '0'
        
    def numberButton(self,n):
        self.num.append(str(n))
        self.ans = ''.join(self.num)

    def plusButton(self):
        self.history = float(''.join(self.num))
        self.num = []
        self.operator = '+'

    def minusButton(self):
        self.history = float(''.join(self.num))
        self.num = []
        self.operator = '-'

    def multipleButton(self):
        self.history = float(''.join(self.num))
        self.num = []
        self.operator = '*'

    def divideButton(self):
        self.history = float(''.join(self.num))
        self.num = []
        self.operator = '/'

    def equalButton(self):
        now = float(''.join(self.num))
        if self.operator == '+':
            self.history += now
            if self.history == int(self.history):
                self.history = int(self.history)
            self.ans = str(self.history)
            self.num = [str(self.history)]
            self.operator = ''

        elif self.operator == '-':
            self.history -= now
            if self.history == int(self.history):
                self.history = int(self.history)
            self.ans = str(self.history)
            self.num = [str(self.history)]
            self.operator = ''

        elif self.operator == '*':
            self.history *= now
            if self.history == int(self.history):
                self.history = int(self.history)
            self.ans = str(self.history)
            self.num = [str(self.history)]
            self.operator = ''

        elif self.operator == '/':
            self.history /= now
            if self.history == int(self.history):
                self.history = int(self.history)
            self.ans = str(self.history)
            self.num = [str(self.history)]
            self.operator = ''

        else:
            pass
        
        

class CalculatorApp(App):
    title = '電卓'
    def build(self):
        return Calculator()
    pass

if __name__ == '__main__':
    CalculatorApp().run()