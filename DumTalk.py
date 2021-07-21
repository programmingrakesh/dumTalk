import pyttsx3
from kivy.lang import Builder
from kivymd.app import MDApp

#from kivy.core.window import Window
#Window.size = (305, 400)


KIVY = """
MDFloatLayout:
    MDLabel:
        text: "Made By S.B. Subbu Rakesh"
        pos_hint: {"center_y": .10}
        halign: "center"
        bold: False
    MDLabel:
        text: "Speak to Everyone"
        pos_hint: {"center_y": .65}
        halign: "center"
        bold: True
        font_style: "H3"
    MDTextField:
        id: text
        hint_text: "Enter The Text to speak"
        size_hint_x: .8
        pos_hint:{"center_x": .5, "center_y": .5}
        bold: True       
    MDRaisedButton:
        text: "Speak"
        size_hint_x: .5
        pos_hint:{"center_x": .5, "center_y": .35}
        on_release: app.Talk()
"""


class MyApp(MDApp):
    e = pyttsx3.init()
    voice = e.getProperty('voices')
    e.setProperty('voice', voice[1].id)
    e.setProperty('rate', 150)

    def build(self):
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        info = Builder.load_string(KIVY)
        return info


    def Talk(self):
        self.e.say(self.root.ids.text.text)
        self.e.runAndWait()

if __name__ == "__main__":
    app = MyApp()
    app.run()
