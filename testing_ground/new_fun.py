from kivymd.app import MDApp
from kivy.properties import ListProperty, StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.lang.builder import Builder

from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout

from kivymd.uix.button import MDButton
from kivymd.uix.textfield import MDTextField

from kivy.uix.button import Button


class BoxFormula(MDBoxLayout):
    columns = NumericProperty(2)
    rows = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(self.rows):
            self.add_widget(Box(columns=self.columns))


class Box(MDBoxLayout):
    columns = NumericProperty(2)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(self.columns):
            mini_box = MiniBox(on_release=self.remove_container)
            self.add_widget(mini_box)

    def get_data(self):
        if self.children:
            data = [i.text for i in self.children]
            data.reverse()
            return data

    def remove_container(self, container, *args):
        self.remove_widget(container)


class MiniBox(MDBoxLayout):
    hide_button = BooleanProperty(False)
    saved_button = ObjectProperty()

    def __init__(self, **kwargs):
        self.register_event_type("on_release")
        super().__init__(**kwargs)

        self.ids["button"].bind(on_release=lambda _: self.dispatch("on_release"))
        self.hide_button = True

    def on_release(self, *args):
        pass

    def on_hide_button(self, object, bool_value, *args):
        if bool_value and self.saved_button in self.children:
            self.remove_widget(self.saved_button)

        elif not bool_value and self.saved_button not in self.children:
            self.add_widget(self.saved_button, 2)


class ScreenStart(MDScreen):
    container_box = ObjectProperty()
    title_name = StringProperty()

    def get_data(self):
        data = []
        for i in self.container_box.children:
            if type(i) is Box:
                data.append(i.get_data())
        data.reverse()
        return data


class RootWidget(MDScreenManager):
    pass


class NewFun(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("components.kv")
        self.root_widget = RootWidget()
        self.screen_start = ScreenStart(title_name="AppBar small")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.root_widget.add_widget(self.screen_start)
        self.screen_start.container_box.add_widget(MDButton(on_release=self.test))

        for i in range(5):
            self.screen_start.container_box.add_widget(Box(columns=3))

        self.screen_start.container_box.add_widget(BoxFormula(columns=5, rows=3))
        return self.root_widget

    def test(self, *args):
        data = self.screen_start.get_data()
        print(data)


if __name__ == '__main__':
    NewFun().run()
