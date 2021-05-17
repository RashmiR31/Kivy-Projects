from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.spelling import Spelling
from kivy.core.window import Window

Builder.load_file('slider.kv')

class mylayout(Widget):
    def slide_it(self,*args):
       #print(args[1])
       self.slide_text.text = str(int(args[1]))
       self.slide_text.font_size = str(int(args[1])*5)


class SpellCheck(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return mylayout()

if __name__ == '__main__':
    SpellCheck().run()