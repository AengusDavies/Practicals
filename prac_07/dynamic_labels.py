"""
CP1404/CP5632 Practical
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Program that uses dynamic widgets to print names from list"""
    output_names = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Eeny', 'Meeny', 'Miny', 'Moe']

    def build(self):
        """Builds the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_names()
        return self.root

    def create_names(self):
        """Create labels within the Kivy GUI of each name from the list"""
        for name in self.names:
            new_label = Label(text=name)
            # new_label.bind(on_release=self.press_entry)
            self.root.ids.names_box.add_widget(new_label)
            self.output_names = name


DynamicLabelsApp().run()
