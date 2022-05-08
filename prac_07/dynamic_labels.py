from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self):
        super().__init__()
        self.list_of_names = ["Name 1", "Name 2", "Name 3", "Name 4"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.list_of_names:
            temp_label = Label(text=name)
            self.root.ids.dynamic_labels.add_widget(temp_label)

DynamicLabelsApp().run()