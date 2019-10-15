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
from kivy.properties import StringProperty
from kivy.uix.image import Image
Window.size = (dp(720),dp(1280))

class Table(AnchorLayout):
    pass
class Register(ModalView):
    pass
class Player_BJ(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.chips = 2000
        self.widget = Player_Box(name = self.name,chips = str(self.chips))
class Player_Box(AnchorLayout):
    name = StringProperty()
    chips = StringProperty()
class MainApp(App):
    def build(self):
        self.main_widget = Builder.load_file('main.kv')
        self.start_button = StartButton(size_hint = [None,None])
        self.main_widget.ids.table.add_widget(self.start_button)
        return self.main_widget
    def register(self):
        register = Register()
        register.open()
    def remove_start_button(self):
        self.main_widget.ids.table.remove_widget(self.start_button)
    def greate_player(self,name):
        self.player = Player_BJ(name)
        self.main_widget.ids.table.add_widget(self.player.widget)

class StartButton(AnchorLayout):
    pass
MainApp().run()