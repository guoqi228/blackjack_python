import numpy as np
class Deck():

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    numbers = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
    deck = []

    def __init__(self, num):
        self.num = num

    def shuffle_deck(self, alist):
        n = len(alist)
        return np.random.choice(alist, n, replace=False).tolist()

    def create_deck(self):
        Deck.deck = []
        for i in range(self.num):
            for suit in Deck.suits:
                for number in Deck.numbers:
                    Deck.deck.append(str(number) + ' ' + 'of' + ' '+ suit)
        Deck.deck = self.shuffle_deck(Deck.deck)

    def pop_deck(self):
        return Deck.deck.pop()

    def check_deck(self):
        if len(Deck.deck) == 0:
            self.create_deck()  
