from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ListProperty, StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.uix.button import Button


class Box(MDBoxLayout):
    def get_data(self):
        if self.children:
            return [i.text for i in self.children]


class ScreenStart(MDScreen):
    container_box = ObjectProperty()
    title_name = StringProperty()

    def get_data(self):
        data = []
        for i in self.container_box.children:
            if type(i) is Box:
                data.append(i.get_data())
        return data


class RootWidget(MDScreenManager):
    pass


class NewFun(MDApp):
    def __init__(self, **kvargs):
        super().__init__(**kvargs)
        self.root_widget = RootWidget()
        self.screen_start = ScreenStart(title_name="AppBar small")
        # self.root_widget.add_widget(self.screen_start)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        m = MDScreenManager()
        s = MDScreen()
        s.add_widget(Button())
        m.add_widget(s)
        return m


if __name__ == '__main__':
    NewFun().run()
