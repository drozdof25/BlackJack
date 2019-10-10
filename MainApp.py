from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from blackjack import Player
from kivy.uix.image import Image
Window.size = (dp(720),dp(1280))

class Table(Image):
    pass
class Player():
    def __init__(self,name):
        self.name = name
        self.chips = 2350
class Player_Box(Image):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.player = Player('Dimon')
        self.chips = self.player.chips
class MainApp(App):
    def build(self):
        self.main_widget = Builder.load_file('main.kv')
        return self.main_widget
MainApp().run()