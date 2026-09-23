from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.popup import Popup
from kivy.core.window import Window


class CalculatorApp(App):

    def build(self):
        Window.clearcolor = (0.125, 0.129, 0.141, 1)

        main = BoxLayout(
            orientation="vertical",
            padding=12,
            spacing=8
        )

        self.entry = TextInput(
            text="",
            font_size=32,
            halign="right",
            multiline=False,
            readonly=True,
            size_hint_y=0.18,
            background_color=(0.188, 0.192, 0.204, 1),
            foreground_color=(1, 1, 1, 1)
        )

        main.add_widget(self.entry)

        buttons = [
            ("C", (0.85, 0.33, 0.31, 1)),
            ("⌫", (0.37, 0.39, 0.42, 1)),
            ("/", (0.94, 0.65, 0.0, 1)),
            ("*", (0.94, 0.65, 0.0, 1)),

            ("7", (0.24, 0.25, 0.26, 1)),
            ("8", (0.24, 0.25, 0.26, 1)),
            ("9", (0.24, 0.25, 0.26, 1)),
            ("-", (0.94, 0.65, 0.0, 1)),

            ("4", (0.24, 0.25, 0.26, 1)),
            ("5", (0.24, 0.25, 0.26, 1)),
            ("6", (0.24, 0.25, 0.26, 1)),
            ("+", (0.94, 0.65, 0.0, 1)),

            ("1", (0.24, 0.25, 0.26, 1)),
            ("2", (0.24, 0.25, 0.26, 1)),
            ("3", (0.24, 0.25, 0.26, 1)),
            ("=", (0.20, 0.66, 0.33, 1)),

            ("0", (0.24, 0.25, 0.26, 1)),
            (".", (0.24, 0.25, 0.26, 1))
        ]

        grid = GridLayout(
            cols=4,
            spacing=6,
            size_hint_y=0.65
        )

        for text, color in buttons:
            button = Button(
                text=text,
                font_size=22,
                bold=True,
                color=(1, 1, 1, 1),
                background_normal="",
                background_color=color
            )

            button.bind(
                on_press=lambda instance, value=text:
                self.click(value)
            )

            grid.add_widget(button)

        main.add_widget(grid)

        color_button = Button(
            text="🎨  انتخاب رنگ پس زمینه",
            font_size=17,
            bold=True,
            size_hint_y=0.12,
            background_normal="",
            background_color=(0.37, 0.39, 0.42, 1)
        )

        color_button.bind(on_press=self.open_color_picker)

        main.add_widget(color_button)

        return main

    def click(self, text):

        if text == "C":
            self.entry.text = ""

        elif text == "⌫":
            self.entry.text = self.entry.text[:-1]

        elif text == "=":
            try:
                expression = self.entry.text
                result = eval(expression, {"__builtins__": None}, {})
                self.entry.text = str(result)
            except:
                self.entry.text = "خطا"

        else:
            self.entry.text += text

    def open_color_picker(self, instance):

        picker = ColorPicker()

        popup = Popup(
            title="انتخاب رنگ پس زمینه",
            content=picker,
            size_hint=(0.9, 0.8)
        )

        def change_color(instance, color):
            Window.clearcolor = color

        picker.bind(color=change_color)

        popup.open()


if __name__ == "__main__":
    CalculatorApp().run()
