"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MilesKmApp(App):
    output_text = StringProperty()
    """A Kivy app for converting miles to km"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):

    def handle_increment(self, value):
        pass


MilesKmApp().run()
