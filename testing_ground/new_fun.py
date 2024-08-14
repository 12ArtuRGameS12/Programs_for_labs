from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ListProperty, StringProperty, BooleanProperty, NumericProperty, ObjectProperty


class Box(MDBoxLayout):
    def get_data(self):
        if self.children:
            for i in self.children:
                print(i.text)


class ScreenStart(MDScreen):
    container_box = ObjectProperty()
    title_name = StringProperty()


class RootWidget(MDScreenManager):
    pass


class NewFun(MDApp):
    # def __init__(self, **kvargs):
    #     super().__init__(**kvargs)
    #     self.root_widget = RootWidget()
    #     self.screen_start = ScreenStart(title_name="AppBar small")
    #     self.root_widget.add_widget(self.screen_start)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        # return self.root_widget


if __name__ == '__main__':
    NewFun().run()
