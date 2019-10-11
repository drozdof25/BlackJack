class Card():
    ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['h','d','c','s']
    def __init__(self,rank,suit,face_up = True):
        self.rank = rank
        self.suit = suit
        self.card = self.rank + self.suit
        self.face_up = face_up
    def flip(self):
        self.face_up = not self.face_up
class Hand():
    def __init__(self):
        self.cards =[]
    def add(self,card):
        self.cards.append(card)
    def clear(self):
        self.cards = []
class Deck(Hand):
    def populate(self):
        for rank in Card.ranks:
            for suit in Card.suits:
                self.add(Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self,hand,count_card):
        for i in range(0,count_card):
            if self.cards:
                hand.add(self.cards.pop())
            else:
                print('Карты закончились')
