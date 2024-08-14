from kivymd.app import MDApp
from kivymd.uix.filemanager.filemanager import MDFileManager


class NewFunf(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"


if __name__ == '__main__':
    NewFunf().run()
