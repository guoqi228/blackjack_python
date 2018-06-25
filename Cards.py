class Cards():

    @classmethod
    def get_points(cls, cards):
        sum_points = 0
        ace_counts = 0
        card_list = []
        for card in cards:
            if card[0] == 'A':
                ace_counts += 1
            elif card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
                card_list.append(10)
            else:
                card_list.append(int(card[0:2]))
        #print(card_list)
        sum_points = sum(card_list)
        for i in range(ace_counts):
            if sum_points + 11 > 21:
                sum_points += 1
            elif sum_points + 11 <= 21:
                sum_points += 11
        return sum_points

    @classmethod
    def check_points(cls, points):
        if points > 21:
            return 0
        elif points < 17:
            return 1
        elif 18 <= points <= 20:
            return 2
        elif points == 21:
            return 3
