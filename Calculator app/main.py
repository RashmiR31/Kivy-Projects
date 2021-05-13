from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#App size
Window.size=(500,600)

#design file 
Builder.load_file('calc.kv')

class mylayout(Widget):
    def clear(self):
        self.ids.calc_input.text='0'

    def button_press(self,button):
        #create a variable that contains whatever in the textbox already
        prior = self.ids.calc_input.text

        #test for error
        if "Error" in prior:
            prior=''
        if prior == "0":
            self.ids.calc_input.text=''
            self.ids.calc_input.text= f'{button}'
        else:
            self.ids.calc_input.text=f'{prior}{button}'

    def math_sign(self,sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = f'{answer}'
        except:
            self.ids.calc_input.text="Error"
        
        #addition
        """
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            # loop thrugh num_list
            for number in num_list:
                answer = answer + float(number)
            self.ids.calc_input.text = f'{answer}'
        """
    def dot(self):
        prior = self.ids.calc_input.text
        num_list= prior.split("+")
        
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text=prior
        elif "." in prior:
            pass
        else:
        # add a period at the end of text
            prior = f'{prior}.'
            self.ids.calc_input.text=prior

    def remove(self):
        prior = self.ids.calc_input.text
        #remove last item in the textbox
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else: 
            self.ids.calc_input.text = f'-{prior}'








class Calculator(App):
    def build(self):
        return mylayout()

if __name__ == '__main__':
    Calculator().run()