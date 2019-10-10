from cards import Card,Deck,Hand
class BJ_Card(Card):
    ace_value = 1
    @property
    def value(self):
        if self.face_up:
            if BJ_Card.ranks.index(self.rank)+1>10:
                val = 10
            else:
                val = BJ_Card.ranks.index(self.rank)+1
        else:
            val = None
        return val
class BJ_Deck(Deck):
    def populate(self):
        for rank in BJ_Card.ranks:
            for suit in BJ_Card.suits:
                self.add(BJ_Card(rank,suit))
class BJ_Hand(Hand):
    @property
    def total_value(self):
        total = 0
        for card in self.cards:
            if not card.value:
                return 0
        for card in self.cards:
            total += card.value
        check_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ace_value:
                check_ace = True
        if check_ace and total <= 11:
            total += 10
        return total
    def busted(self):
        return self.total_value > 21
    def __str__(self):
        out = str()
        for card in self.cards:
            if card.face_up:
                out += card.card
            else:
                out += '**'
        out +='  '+str(self.total_value)
        return out
class Player(BJ_Hand):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def check_continue(self):
        return input('Брать карту (y/n): ') == 'y'
    def bust(self):
        print(self.name+ ' перебор.')
        self.lose()
    def lose(self):
        print(self.name+ ' проиграл.')
    def win(self):
        print(self.name+ ' выиграл.')
    def push(self):
        print(self.name + ' ничья')
class Dealer(BJ_Hand):
    def __init__(self):
        super().__init__()
        self.name = 'Дилер'
    def check_continue(self):
        return self.total_value < 17
    def bust(self):
        print(self.name + ' перебор.')
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
class Game():
    def __init__(self,name):
        self.player = Player(name)
        self.dealer = Dealer()
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    def add_cards(self,player):
        while not player.busted() and player.check_continue():
            self.deck.deal(player, 1)
            print(player.name + ' :' + str(player))
            if player.busted():
                player.bust()
    def play(self):
        self.deck.deal(self.player,2)
        self.deck.deal(self.dealer,2)
        self.dealer.flip_first_card()
        print(self.player.name + ' :' + str(self.player))
        print(self.dealer.name + ' :' + str(self.dealer))
        self.add_cards(self.player)
        self.dealer.flip_first_card()
        if not self.player.busted():
            print(self.dealer.name + ' :' + str(self.dealer))
            if self.dealer.check_continue():
                self.add_cards(self.dealer)
            if self.dealer.busted():
                self.player.win()
            elif self.player.total_value == self.dealer.total_value:
                self.player.push()
            elif self.player.total_value > self.dealer.total_value:
                self.player.win()
            elif self.player.total_value < self.dealer.total_value:
                self.player.lose()
        self.player.clear()
        self.dealer.clear()