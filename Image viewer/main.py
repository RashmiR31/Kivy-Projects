from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('menu.kv')

class mylayout(Widget):
    def selected(self,filename):
        try:
            self.ids.my_image.source=filename[0]
        except:
            pass


class imageviewer(App):
    def build(self):
        return mylayout()

if __name__ == '__main__':
    imageviewer().run()

