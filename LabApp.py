from kivy.app import App
import lib_lab as lb


def clear(a):
    x = True if a.find(",") != -1 else False
    y = True if a.find(".") != -1 else False
    a = lb.clr_sp(a)
    a = [float(i) for i in a.split()]
    return a


class MyApp(App):
    def calc1(self, text_input):
        try:
            if all(i.text == "" for i in text_input[:-1]): raise Exception("")
            x = clear(text_input[0].text)
            y = float(text_input[1].text)
            z = int(text_input[2].text) if len(text_input[2].text) else 2
            x1 = lb.prim_izmer(x, y, z)
            x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)

    def calc2(self, text_input):
        try:
            if all(i.text == "" for i in text_input[:-1]): raise Exception("")
            x = clear(text_input[0].text)
            y = clear(text_input[1].text)

            x1 = lb.mnc(x, y)
            x2 = f"y=ax+b\nR = {x1[0]}\na = {x1[1][0]}\nda = {x1[1][1]}\nb = {x1[2][0]}\ndb = {x1[2][1]}"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)

    def calc3(self, text_input):
        try:
            if all(i.text == "" for i in text_input[:-1]): raise Exception("")
            x = clear(text_input[0].text)
            y = clear(text_input[1].text)

            x1 = lb.nerav_izmer(x, y)
            x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
            text_input[-1].text = x2
        except Exception as err:
            text_input[-1].text = str(err)


MyApp().run()
