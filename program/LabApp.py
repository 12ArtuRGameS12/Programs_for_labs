from kivymd.app import MDApp

from kivy.properties import ListProperty, StringProperty, BooleanProperty, NumericProperty

from kivy.uix.togglebutton import ToggleButton
from kivymd.uix.list.list import MDListItem
from kivymd.uix.screen import MDScreen

import lib_lab as lb


class ScreenGuide(MDScreen):
    text = StringProperty()

    def on_text(self, *args):
        match self.text:
            case "Прямые измерения":
                a = "1"
            case "МНК":
                a = "2"
            case "Неравноточные измерения":
                a = "3"
            case "Статистика":
                a = "4"
            case "Косвенные измерения":
                a = "5"
            case "Формулы exe":
                a = "6"
            case _:
                a = ""
        self.ids["my"].text = open(f"program/text/guide{a}.txt", encoding="utf-8").read()\
            if a else ""


class MyToggleButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(state=self.chec_state)

        self.text_down = self.text
        self.text_normal = self.text
        # self.chec_state(self, self.state)

    def chec_state(self, _, value):
        if value == "down":
            self.text = self.text_down
        else:
            self.text = self.text_normal


def clear(a):
    return [lb.convert2number(i) for i in lb.clr_sp(a).split()]


class MyApp(MDApp):
    last_screen = ListProperty()
    dev = BooleanProperty(False)
    interval = NumericProperty(2)
    cc1 = NumericProperty(1)

    def build(self):
        self.theme_cls.theme_style = "Dark"

    def calc1(self, text_input, output):
        try:
            if all(i == "" for i in text_input): raise Exception("")

            x = clear(text_input[0].replace(",", "."))
            y = clear(text_input[1].replace(",", "."))[0]

            x1 = lb.prim_izmer(data=x, accuracy=y, interval=self.interval, debug=self.dev)
            if not self.dev:
                x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
            else:
                x2 = ""
                for i in x1: x2 += i + ": " + str(x1[i]) + "\n"
            output.text = x2
        except Exception as err:
            output.text = str(err)

    def calc2(self, text_input, mode, output):
        try:
            if all(i == "" for i in text_input): raise Exception("")
            x = clear(text_input[0].replace(",", "."))
            y = clear(text_input[1].replace(",", "."))

            x1 = lb.mnc(arg1=x, arg2=y, interval=self.interval, mode=mode, debug=self.dev)
            if not self.dev:
                if mode == 1:
                    x2 = f"y=ax+b\nR = {x1[0]}\na = {x1[1][0]}\nda = {x1[1][1]}\nb = {x1[2][0]}\ndb = {x1[2][1]}"
                else:
                    x2 = f"y=ax\nR = {x1[0]}\na = {x1[1][0]}\nda = {x1[1][1]}"
            else:
                x2 = ""
                for i in x1: x2 += str(i) + ": " + str(x1[i]) + "\n"
            output.text = x2
        except Exception as err:
            output.text = str(err)

    def calc3(self, text_input, output):
        try:
            if all(i == "" for i in text_input): raise Exception("")
            x = clear(text_input[0].replace(",", "."))
            y = clear(text_input[1].replace(",", "."))

            x1 = lb.nerav_izmer(data=x, errors=y, debug=self.dev)
            if not self.dev:
                x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
            else:
                x2 = ""
                for i in x1: x2 += i + ": " + str(x1[i]) + "\n"
            output.text = x2
        except Exception as err:
            output.text = str(err)

    def calc4(self, text_input, output):
        try:
            if all(i == "" for i in text_input): raise Exception("")
            x = clear(text_input[0].replace(",", "."))

            if text_input[1]:
                y = clear(text_input[1].replace(",", "."))
                x1 = lb.stat(x, y)
            else:
                x1 = lb.stat(x)
            x2 = ""
            for i in x1: x2 += i + ": " + str(x1[i]) + "\n"
            output.text = x2
        except Exception as err:
            output.text = str(err)

    def calc5(self, text_input, output):
        try:
            if all(i == "" for i in text_input): raise Exception("")
            x = text_input[0]
            y = text_input[1].split()

            x1 = lb.cosn_izmer_formula(x, *y)
            output.text = x1
        except Exception as err:
            output.text = str(err)

    def calc6(self, text_input, output):
        try:
            if all(i == "" for i in text_input): raise Exception("")
            x = text_input[0]
            y = (i.split("=") for i in lb.clr_sp(text_input[1], "=").split())
            y = {i[0]: i[1] for i in y}
            x1 = lb.formula_exe(x, y)
            x2 = ""
            for i in x1: x2 += str(i) + "\n"
            output.text = x2
        except Exception as err:
            output.text = str(err)
