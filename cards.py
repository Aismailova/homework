import random

RANKS = ['heart', 'diamonds', 'spades', 'clubs']
SUITS = ['Ace', 'King', 'Queen', 'Jack','10','9','8','7','6','5','4','3','2']

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        c = self.suit + " " + self.rank
        return c

class Joker(Card):
    def __init__(self,suit="", rank="Joker"):
        self.rank = "Joker"
        self.suit = ""

class Deck():
    def __init__(self):
        self.contents = []
        self.contents = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.contents.append(Joker())
        self.contents.append(Joker())
        for item in self.contents:
            print(item)
    def shuffle(self):
        random.shuffle(self.contents)
        for item in self.contents:
            print(item)


class Hand(Deck):
    def __init__(self, number, deck):
        self.hand_contents = []
        for i in range(number):
            self.hand_contents.append(random.choice(deck.contents))
        for item in self.hand_contents:
            print(item)

answer = input("Would yo like to start a game? Please, enter Y/N: ")

if answer.lower() == 'y':
    d = Deck()
    d.shuffle()

n_of_cards_in_hand = int(input("How much card do you need? From 1 to 54: "))

h = Hand(n_of_cards_in_hand,d)

