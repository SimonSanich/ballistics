from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from s60_calculator import calculate_trajectory

SHELLS = {
 "OF-57": {"v0": 1000},
 "BR-281": {"v0": 1010}
}
class BallisticApp(App):
    def build(self):
        return BoxLayout()
def calculate(self):
    distance = float(self.root.ids.distance_input.text)
    angle = float(self.root.ids.angle_input.text)
    shell = self.root.ids.shell_spinner.text
    v0 = SHELLS[shell]["v0"]

    time, height = calculate_trajectory(v0, angle, distance)
    result = f"Час польоту: {time} с\nВисота: {height} м"
    self.root.ids.result_label.text = result
if __name__ == "__main__":
    BallisticApp().run()
