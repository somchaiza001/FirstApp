from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

KV = """

"""

class MyApp(App):
	def build(self):
		la = BoxLayout(orientation="vertical")
		lb = Label(text="Hello World")
		la.add_widget(lb)
		return la

if __name__ == "__main__":	
	MyApp().run()