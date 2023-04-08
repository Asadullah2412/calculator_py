from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


class Calculator(BoxLayout):
    question_label = StringProperty("Question")
    answer_label = StringProperty("Answer")

    def button1(self):
        self.question_label = "1"


class MainCalulator(App):
    pass


MainCalulator().run()
