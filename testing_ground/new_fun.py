from kivymd.app import MDApp
from kivy.properties import ListProperty, StringProperty, BooleanProperty, NumericProperty, ObjectProperty
from kivy.lang.builder import Builder

from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.anchorlayout import MDAnchorLayout

from kivymd.uix.button import MDButton, MDButtonText, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.widget import MDWidget

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
    hide_button = BooleanProperty(True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        button = MDIconButton(icon="plus")
        button.bind(on_release=self.add_container)
        self.saved_button = button

        for i in range(self.columns):
            self.add_container()

    def get_data(self):
        if self.children:
            data = [i.get_data() for i in self.children if type(i) is MiniBox]
            data.reverse()
            return data

    def remove_container(self, container, *_):
        index = self.children.index(container)
        self.remove_widget(container)
        return index

    def add_container(self, *_):
        mini_box = MiniBox(on_release=self.remove_container)
        mini_box.hide_button = self.hide_button
        self.add_widget(mini_box)

        if not self.hide_button and self.saved_button in self.children:
            self.remove_widget(self.saved_button)
            self.add_widget(self.saved_button)

    def on_hide_button(self, _object, bool_value, *_):
        for i in self.children:
            i.hide_button = bool_value

        if bool_value and self.saved_button in self.children:
            self.remove_widget(self.saved_button)

        elif not bool_value and self.saved_button not in self.children:
            self.add_widget(self.saved_button)


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

    def on_hide_button(self, _object, bool_value, *_):
        if bool_value and self.saved_button in self.children:
            self.remove_widget(self.saved_button)
            # self.padding = (0, 0)
            # self.spacing = 0
        elif not bool_value and self.saved_button not in self.children:
            self.add_widget(self.saved_button, 2)
            # self.padding = (0, 5)
            # self.spacing = 30

    def get_data(self):
        return self.ids["text_field"].text


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
        self.screen_start.container_box.add_widget(MDButton(MDButtonText(text="get_data"), on_release=self.test))
        self.screen_start.container_box.add_widget(MDButton(MDButtonText(text="edit"), on_release=self.test2))

        for i in range(5):
            self.screen_start.container_box.add_widget(Box(columns=3))

        # self.screen_start.container_box.add_widget(BoxFormula(columns=5, rows=3))
        return self.root_widget

    def test(self, *args):
        data = self.screen_start.get_data()
        print(data)

    def test2(self, *args):
        for i in self.screen_start.container_box.children:
            if type(i) is Box:
                i.hide_button = not i.hide_button


if __name__ == '__main__':
    NewFun().run()
