"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

KM_MULTIPLIER = 1.60934


class MilesKmApp(App):
    output_text = StringProperty()
    """A Kivy app for converting miles to km"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        """Handle calculation for converting miles to kilometres"""
        result = value * KM_MULTIPLIER
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value):
        pass


MilesKmApp().run()
