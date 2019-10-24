from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from blackjack import Player,BJ_Card,Dealer,BJ_Deck
from kivy.properties import StringProperty,NumericProperty,ListProperty
from kivy.uix.image import Image
Window.size = (dp(720),dp(1280))

class Table(AnchorLayout):
    pass
class Register(ModalView):
    pass
class BetSelecter(ModalView):
    bet = NumericProperty(200)
class Player_BJ(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.chips = 2000
        self.widget = Player_Box(name = self.name,chips = str(self.chips))
class Player_Box(AnchorLayout):
    name = StringProperty()
    chips = StringProperty()
class Card_Box(FloatLayout):
    cards = StringProperty()
    position = ListProperty()
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
    def change_bet(self):
        betselekter = BetSelecter()
        betselekter.open()
    def betting(self,pot):
        self.pot = pot
        self.player.chips -= pot
        self.player.widget.chips = str(self.player.chips)
    def add_pot_label(self):
        pot_lbl = PotLabel(pot = self.pot)
        self.main_widget.ids.table.add_widget(pot_lbl)
    def start_game(self):
        self.deck = BJ_Deck()
        self.dealer = Dealer()
        self.deck.populate()
        self.deck.shuffle()
        self.deck.deal(self.player,2)
        self.deck.deal(self.dealer, 2)
        self.dealer.flip_first_card()
        card_box_player = Card_Box(position=[250,325],cards = str(self.player))
        card_box_dealer = Card_Box(position=[250,850],cards = str(self.dealer))
        self.main_widget.ids.table.add_widget(card_box_player)
        self.main_widget.ids.table.add_widget(card_box_dealer)
        btn1 = Button(text='Взять карту')
        btn2 = Button(text='Хватит')
        self.main_widget.ids.bl.add_widget(btn1)
        self.main_widget.ids.bl.add_widget(btn2)
class StartButton(AnchorLayout):
    pass
class PotLabel(AnchorLayout):
    pot = NumericProperty()
MainApp().run()