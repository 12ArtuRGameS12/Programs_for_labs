from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
import lib_lab as lb


class MyTextInput(TextInput):
    def on_double_tap(self):
        self._select_word(delimiters=u' :;!?\'"<>()[]{}')


def clear(a):
    return [lb.convert2number(i) for i in lb.clr_sp(a).split()]


class MyApp(App):
    def test(*args, **kargs):
        print(args)
        print(kargs)

    def calc1(self, text_input, dev):
        try:
            x0 = text_input[-2].children
            y0 = len(x0) // 2
            z = 0
            for i in range(y0):
                if x0[i].active:
                    z = abs(y0 - i)
                    break
            if all(i.text == "" for i in text_input[:-2]): raise Exception("")
            x = clear(text_input[0].text.replace(",", "."))
            y = lb.convert2number(text_input[1].text.replace(",", "."))
            x1 = lb.prim_izmer(x, y, z, dev)
            if not dev:
                x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
            else:
                x2 = ""
                for i in x1: x2 += i + ": " + str(x1[i]) + "\n"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)

    def calc2(self, text_input, dev):
        try:
            x0 = text_input[-2].children
            y0 = len(x0) // 2
            z = 0
            for i in range(y0):
                if x0[i].active:
                    z = abs(y0 - i)
                    break
            if all(i.text == "" for i in text_input[:-2]): raise Exception("")
            x = clear(text_input[0].text.replace(",", "."))
            y = clear(text_input[1].text.replace(",", "."))

            x1 = lb.mnc(x, y, z, dev)
            if not dev:
                if z == 1:
                    x2 = f"y=ax+b\nR = {x1[0]}\na = {x1[1][0]}\nda = {x1[1][1]}\nb = {x1[2][0]}\ndb = {x1[2][1]}"
                else:
                    x2 = f"y=ax\nR = {x1[0]}\na = {x1[1][0]}\nda = {x1[1][1]}"
            else:
                x2 = ""
                for i in x1: x2 += i + ": " + str(x1[i]) + "\n"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)

    def calc3(self, text_input, dev):
        try:
            if all(i.text == "" for i in text_input[:-1]): raise Exception("")
            x = clear(text_input[0].text.replace(",", "."))
            y = clear(text_input[1].text.replace(",", "."))

            x1 = lb.nerav_izmer(x, y, dev)
            if not dev:
                x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
            else:
                x2 = ""
                for i in x1: x2 += i + ": " + str(x1[i]) + "\n"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)

    def calc4(self, text_input):
        try:
            if all(i.text == "" for i in text_input[:-1]): raise Exception("")
            x = clear(text_input[0].text.replace(",", "."))
            y = clear(text_input[1].text.replace(",", "."))

            x1 = lb.stat(x, y)
            x2 = ""
            for i in x1: x2 += i + ": " + str(x1[i]) + "\n"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)

    def calc5(self, text_input):
        try:
            if all(i.text == "" for i in text_input[:-1]): raise Exception("")
            x = text_input[0].text
            y = text_input[1].text.split()

            x1 = lb.cosn_izmer_formula(x, *y)
            text_input[-1].text = x1
        except Exception as err:
            text_input[-1].text = str(err)

    def calc6(self, text_input):
        try:
            if all(i.text == "" for i in text_input[:-1]): raise Exception("")
            x = text_input[0].text
            y = (i.split("=") for i in lb.clr_sp(text_input[1].text, "=").split())
            y = {i[0]: i[1] for i in y}
            x1 = lb.formul_exe(x, y)
            x2 = ""
            for i in x1: x2 += str(i) + "\n"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)


MyApp().run()
