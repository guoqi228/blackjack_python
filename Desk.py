class Desk():

    def __init__(self, dealer, player, bots):
        self.dealer = dealer
        self.player = player
        self.bots = bots

    def show_desk(self):
        #print('==========================================')
        #print('Blackjack')
        #print('==========================================')
        self.dealer.show_cards()
        self.player.show_cards()
        for bot in self.bots:
            bot.show_cards()

    def hide_desk(self):
        self.dealer.hide_cards()
        self.player.show_cards()
        for bot in self.bots:
            bot.show_cards()
