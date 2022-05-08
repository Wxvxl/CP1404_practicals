from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesToKmConverter(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increments(self, miles, increments):
        try:
            result = float(miles) + increments
            self.root.ids.input_miles.text = str(result)

        except ValueError:
            if increments == 1:
                self.root.ids.input_miles.text = "1.0"
            if increments == -1:
                self.root.ids.input_miles.text = "-1.0"

    def convert_miles_to_km(self, miles):
        MILES_TO_KM = 1.60934
        try:
            kilometer = float(miles) * MILES_TO_KM
            self.root.ids.output_km.text = str(kilometer)
        except ValueError:
            self.root.ids.output_km.text = "0"


MilesToKmConverter().run()

