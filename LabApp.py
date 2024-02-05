import traceback

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.clock import Clock

import lib_lab as lb


class TextInputFixed(TextInput):
    def on_focus(self, instance, value, *args):
        if value:
            Clock.schedule_once(self.create_keyboard, .1)
        else:
            self.hide_keyboard()

    def create_keyboard(self, *args):
        self.show_keyboard()

    def remove_focus_decorator(function):
        def wrapper(self, touch):
            if not self.collide_point(*touch.pos):
                self.focus = False
            function(self, touch)

        return wrapper

    @remove_focus_decorator
    def on_touch_down(self, touch):
        super().on_touch_down(touch)


class MyTextInput(TextInputFixed):
    input_type = "text"
    keyboard_suggestions = True
    keyboard_mode = 'managed'

    def on_double_tap(self):
        self._select_word(delimiters=u' :;!?\'"<>()[]{}')


def clear(a):
    return [lb.convert2number(i) for i in lb.clr_sp(a).split()]


class MyApp(App):
    def build(self):
        Window.bind(on_keyboard=self.Android_back_click)

    def Android_back_click(self, window, key, *largs):
        if key == 27:
            self.on_request_close()
            return True

    def on_request_close(self, *args, **kargs):
        self.textpopup(title='Exit', text='Are you sure?')
        return True

    def textpopup(self, title='', text=''):
        """Open the pop-up with the name.

        :param title: title of the pop-up to open
        :type title: str
        :param text: main text of the pop-up to open
        :type text: str
        :rtype: None
        """
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        mybutton = Button(text='OK', size_hint=(1, 0.25))
        box.add_widget(mybutton)
        popup = Popup(title=title, content=box, size_hint=(.4, .4))
        mybutton.bind(on_release=self.stop)
        popup.open()

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
