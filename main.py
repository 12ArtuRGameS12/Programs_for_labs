try:
    import datetime
    import traceback

    print(datetime.datetime.now())

    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    from kivy.uix.label import Label

    import LabApp

except Exception:
    print("=" * 30)
    print(f"{traceback.format_exc()}")
    print("=" * 30)
    with open(f"err.log", "w") as f:
        f.write(f"{datetime.datetime.now()}\n\n{traceback.format_exc()}")


    class ErrApp(App):
        def build(self):
            bl = BoxLayout(orientation="vertical")
            label = Label(text=f"{traceback.format_exc()}", valign="middle", halign="center")
            label.bind(
                width=lambda *x: label.setter('text_size')(label, (label.width, None)),
                texture_size=lambda *x: label.setter('height')(label, label.texture_size[1]))
            bl.add_widget(label)
            bl.add_widget(Button(text="Close", on_press=self.stop, size_hint=(1, .1)))
            return bl


    ErrApp().run()
