from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from blackjack import Player,BJ_Card
from kivy.uix.image import Image
Window.size = (dp(720),dp(1280))

class Table(AnchorLayout):
    pass
class Register(ModalView):
    pass
class MainApp(App):
    def build(self):
        self.main_widget = Builder.load_file('main.kv')
        return self.main_widget
    def register(self):
        register = Register()
        register.open()
MainApp().run()