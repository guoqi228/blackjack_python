class Bot():

    def __init__(self, name, balance = 1000):
        self.name = name
        self.cards = []
        self.points = 0
        self.balance = balance
        self.status = 'Playing'

    def show_cards(self):
        if self.balance < 0:
            print('Balance: $0' + '          Status: ' + self.status)
            print(self.name + ': Player lost all the money! Left the table!')
        else:
            print('Balance: ${}'.format(self.balance) + '          Status: ' + self.status)
            print(self.name + ':', end = ' | ')
            for card in self.cards:
                print(card, end = ' | ')
        print('')
        print('==============' * (len(self.cards) + 1))

    def hit(self, card):
        self.cards.append(card)  
