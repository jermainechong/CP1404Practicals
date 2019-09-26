from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilestoKilometresApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_increment(self):
        new_num = int(self.root.ids.input_number.text)
        self.root.ids.input_number.text = new_num + 1

    def handle_reduction(self, input_number):
        self.root.ids.input_number.text = input_number.text - 1

    def handle_calculate(self, value):
        result = value * 1.60934
        self.root.ids.output_label.text = str("%.3f" % result)


MilestoKilometresApp().run()