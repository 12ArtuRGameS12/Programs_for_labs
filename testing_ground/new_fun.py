from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ListProperty, StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.uix.button import Button
from kivymd.uix.button import MDButton
from kivy.lang.builder import Builder


class Box(MDBoxLayout):
    def get_data(self):
        if self.children:
            data = [i.text for i in self.children]
            data.reverse()
            return data


class ScreenStart(MDScreen):
    container_box = ObjectProperty()
    title_name = StringProperty()

    def get_data(self, *args):
        data = []
        for i in self.container_box.children:
            if type(i) is Box:
                data.append(i.get_data())
        data.reverse()
        print(data)
        return data


class RootWidget(MDScreenManager):
    pass


class NewFun(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("components.kv")
        self.root_widget = RootWidget()
        self.screen_start = ScreenStart(title_name="AppBar small")
        self.root_widget.add_widget(self.screen_start)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        for i in range(5):
            self.screen_start.container_box.add_widget(Box())
        d = MDButton()
        d.bind(on_release=self.screen_start.get_data)
        # d.size = (60, 60)
        self.screen_start.container_box.add_widget(d)
        return self.root_widget


if __name__ == '__main__':
    NewFun().run()
