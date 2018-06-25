class Dealer():

    def __init__(self):
        self.cards = []
        self.points = 0
        self.status = 'Playing'
        self.balance = 1000000

    def show_cards(self):
        print('Balance: ${}'.format(self.balance) + '          Status: ' + self.status)
        print('Dealer:', end = ' | ')
        for card in self.cards:
            print(card, end = ' | ')
        print('')
        print('==============' * (len(self.cards) + 1))

    def hide_cards(self):
        print('Balance: ${}'.format(self.balance) + '          Status: ' + self.status)
        print('Dealer: ' + ' | Hidden Card |', end = ' ')
        for card in self.cards[1:]:
            print(card, end = ' | ')
        print('')
        print('==============' * (len(self.cards) + 1))

    def hit(self, card):
        self.cards.append(card)
