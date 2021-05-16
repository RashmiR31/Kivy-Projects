from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.spelling import Spelling
from kivy.core.window import Window

Builder.load_file('spell.kv')

class mylayout(Widget):
    
    def press(self):
        #create instance of spelling
        s = Spelling()
        # select a language
        s.select_language('en_US')

        #See the language options
        #print(s.list_languages())
        #grab word from text box
        word = self.ids.word_input.text

        options = s.suggest(word)
        x = ''
        for item in options:
            x=f'{x} {item}'
        #update our label
        self.ids.word_label.text = f'{x}'


class SpellCheck(App):
    def build(self):
        Window.clearcolor = (0,0,1,1)
        return mylayout()

if __name__ == '__main__':
    SpellCheck().run()