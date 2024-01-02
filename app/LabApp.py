from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from Labs import lib_lab_0_2 as lb


def clear(a):
	x = True if a.find(",") != -1 else False
	y = True if a.find(".") != -1 else False

	while a.find(",") != -1:
		a = a.replace(",", " ")
	while a.find("  ") != -1:
		a = a.replace("  ", " ")
	if a[0] == " ":
		a = a[1:]
	if a[-1] == " ":
		a = a[:-1]
	a = [float(i) for i in a.split()]
	return a


class MyApp(App):

	def __init__(self):
		super().__init__()

		self.sm = ScreenManager(transition=NoTransition())
		text = ("Home", "Прямые измерения", "МНК", "Неравноточные измерения")

		sc = {i: Screen(name=f"{i}") for i in text}
		for i in text: self.sm.add_widget(sc[i])

		bl = {i: BoxLayout(orientation="vertical") for i in text}
		for i in text: sc[i].add_widget(bl[i])

		for i in text[1:]: bl[i].add_widget(Button(text="Home", on_press=self.select))

		bu0 = {i: Button(text=f"{i}", on_press=self.select) for i in text[1:]}
		for i in bu0: bl[text[0]].add_widget(bu0[i])

		self.st1 = (
			TextInput(hint_text="Данные"),
			TextInput(hint_text="Точность прибора"),
			TextInput(hint_text="1=90% 2=95% 3=99 По умолчанию: 2"),
			Label(),
			Button(text="calc", on_press=self.calc1)
		)
		for i in self.st1: bl[text[1]].add_widget(i)

		self.st2 = (
			TextInput(hint_text="x"),
			TextInput(hint_text="y"),
			Label(),
			Button(text="calc", on_press=self.calc2)
		)
		for i in self.st2: bl[text[2]].add_widget(i)

		self.st3 = (
			TextInput(hint_text="Среднее значения"),
			TextInput(hint_text="Погрешность значений"),
			Label(),
			Button(text="calc", on_press=self.calc3)
		)
		for i in self.st3: bl[text[3]].add_widget(i)

	def build(self):
		return self.sm

	def select(self, name):
		self.sm.current = name.text

	def calc1(self, *args, **kwargs):
		try:
			x = clear(self.st1[0].text)
			y = float(self.st1[1].text)
			z = float(self.st1[2].text) if len(self.st1[2].text) != 0 else 2
			x1 = lb.prim_izmer(x, y, z)
			x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
			self.st1[-2].text = x2
		except Exception as err:
			self.st1[-2].text = str(err)

	def calc2(self, *args, **kwargs):
		try:
			x = clear(self.st2[0].text)
			y = clear(self.st2[1].text)

			x1 = lb.naimcv(x, y)
			x2 = f"y=ax+b\nR = {x1[0]}\na = {x1[1][0]}\nda = {x1[1][1]}\nb = {x1[2][0]}\ndb = {x1[2][1]}"
			self.st2[-2].text = x2
		except Exception as err:
			self.st2[-2].text = str(err)

	def calc3(self, *args, **kwargs):
		try:
			x = clear(self.st3[0].text)
			y = clear(self.st3[1].text)

			x1 = lb.nerav_izmer(x, y)
			x2 = f"sred = {x1[0]}\ndelta = {x1[1]}"
			self.st3[-2].text = x2
		except Exception as err:
			self.st3[-2].text = str(err)


MyApp().run()
