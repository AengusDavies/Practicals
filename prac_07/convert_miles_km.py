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
        """Load kv file in order to build Kivy app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self):
        """Handle calculation for converting miles to kilometres"""
        value = self.handle_invalid_input()
        result = value * KM_MULTIPLIER
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, addition):
        """Handle increment of +1 or -1 depending on button pressed was Up or Down"""
        new_value = self.handle_invalid_input() + addition
        self.root.ids.input_number.text = str(new_value)
        self.handle_calculation()

    def handle_invalid_input(self):
        """Handle an invalid input by turning it into a zero"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0.0


MilesKmApp().run()
