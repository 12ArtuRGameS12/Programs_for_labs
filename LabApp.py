# import traceback
# traceback.format_exc()

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton

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
    filt = None

    def insert_text(self, substring, from_undo=False):
        if self.filt:
            x = ""
            for i in substring:
                if i in self.filt:
                    x += i
            substring = x
        return super().insert_text(substring, from_undo=from_undo)

    def on_double_tap(self):
        self._select_word(delimiters=u' :;!?\'"<>()[]{}')


class MyTextInput2(MyTextInput):
    def create_keyboard(self, *args):
        pass


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


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dev = False
        self.interval = 2
        self.last = "Home"
        self.cc1 = 1

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

    def test(self, *args, **kargs):
        print(self, args, kargs)
        for i in self.__dict__: print(i, self.__dict__[i])

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


MyApp().run()
