class Blackjack():


    #all_players = [myplayer]
    exit = False
    while not exit:
        bot1 = Bot('Clay')
        bot2 = Bot('Matt')
        bot3 = Bot('Jamie')
        bots = []

        mydeck = Deck(7)
        mydeck.create_deck()
        myplayer = Player()
        mydealer = Dealer()
        clear_output()
        Welcome.welcome()
        main_menu = Menu('Main Menu', ['Play Alone', 'Add Robot', 'Exit'])
        main_menu.show_menu()
        print('Please enter your option: ')
        option = UserInput.int_input(0, main_menu.menu_length() - 1)
        if option == 0:
            bots = []
        elif option == 1:
            clear_output()
            Welcome.welcome()
            bot_menu = Menu('Add Robot', ['Add 1 robot', 'Add 2 robot', 'Add 3 robot'])
            bot_menu.show_menu()
            print('How many Robots you want to add?')
            bot_option = UserInput.int_input(0, bot_menu.menu_length() - 1)
            if bot_option == 0:
                bots = [bot1]
            elif bot_option == 1:
                bots = [bot1, bot2]
            elif bot_option == 2:
                bots = [bot1, bot2, bot3]
        elif option == 2:
            exit = True
            print('Thanks for playing!')
            print('Exiting game... bye!')
            break

        for bot in bots:
            #all_players.append(bot)
            print('Adding new player...')
            time.sleep(1)
            print(bot.name + ' has joined the game!')
            time.sleep(2)

        player_quit = False
        while not player_quit:

            clear_output()
            Welcome.welcome()
            bet_menu = Menu('Play Option', ['Place $100 bet', 'Leave the table'])
            bet_menu.show_menu()
            print('Your balance: {}'.format(myplayer.balance))
            print('==========================================')
            bet_option = UserInput.int_input(0, bet_menu.menu_length() - 1)
            if bet_option == 0:
                if myplayer.balance < 100:
                    print('You don\'t have enough balance!')
                    print('Good luck next time!')
                    print('Returning to the main menu...')
                    time.sleep(3)
                    player_quit = True
                    break

                curr_players = [mydealer, myplayer]
                total_bet = 200
                myplayer.balance -= 100
                mydealer.balance -= 100
                print('Placing bet...')
                time.sleep(1)
                print('Dealing cards...')
                time.sleep(1)

                for bot in bots:
                    if bot.balance > 100:
                        total_bet += 100
                        bot.balance -= 100
                        curr_players.append(bot)
                    else:
                        bot.status = 'Left'


                for i in range(2):
                    mydealer.hit(mydeck.pop_deck())
                    myplayer.hit(mydeck.pop_deck())
                    for bot in bots:
                        if bot.balance > 100:
                            bot.hit(mydeck.pop_deck())

            #     clear_output()
            #     Welcome.welcome()
            #     mydesk = Desk(mydealer, myplayer, bots)
            #     mydesk.hide_desk()

                all_stay = False
                while not all_stay:
                    clear_output()
                    Welcome.welcome()
                    mydesk = Desk(mydealer, myplayer, bots)
                    mydesk.hide_desk()
                    is_stay = False
                    while not is_stay:
                        hit_menu = Menu('Hit or Stay?', ['Hit', 'Stay'])
                        hit_menu.show_menu()
                        hit_option = UserInput.int_input(0, hit_menu.menu_length() - 1)
                        if hit_option == 0:
                            myplayer.hit(mydeck.pop_deck())
                            if Cards.get_points(myplayer.cards) > 21:
                                clear_output()
                                Welcome.welcome()
                                mydesk.hide_desk()
                                print('You busted!')
                                is_stay = True
                                time.sleep(1)
                                break
                            else:
                                clear_output()
                                Welcome.welcome()
                                mydesk.hide_desk()
                        elif hit_option == 1:
                            clear_output()
                            Welcome.welcome()
                            mydesk.hide_desk()
                            is_stay = True
                            break

                    print('Waiting for other players...')
                    time.sleep(2)
                    for bot in bots:
                        if bot.balance > 100:
                            if Cards.get_points(bot.cards) < 17:
                                bot.hit(mydeck.pop_deck())

                    if Cards.get_points(mydealer.cards) < 17:
                        mydealer.hit(mydeck.pop_deck())

                    all_points = []
                    all_status = []
                    num_blackjack = 0
                    num_bust = 0
                    num_player = len(curr_players)
                    for player in curr_players:
                        if Cards.get_points(player.cards) == 21:
                            num_blackjack += 1
                            player.status = 'Blackjack'
                            all_status.append(player.status)
                            all_points.append(Cards.get_points(player.cards))
                        elif Cards.get_points(player.cards) > 21:
                            player.status = 'Busted'
                            all_status.append(player.status)
                            all_points.append(Cards.get_points(player.cards))
                        else:
                            all_points.append(Cards.get_points(player.cards))
                            all_status.append(player.status)

                    max_point = 0
                    if 'Blackjack' in all_status:
                        for player in curr_players:
                            if player.status == 'Blackjack':
                                player.status = 'Won'
                                player.balance += total_bet / num_blackjack
                            else:
                                player.status = 'Lost'
                    elif 'Blackjack' not in all_status:
                        for player in curr_players:
                            if player.status != 'Busted':
                                if Cards.get_points(player.cards) > max_point:
                                    max_point = Cards.get_points(player.cards)
                            elif player.status == 'Busted':
                                num_bust += 1

                        if num_bust < num_player:
                            num_max = 0
                            winer = []
                            for i, point in enumerate(all_points):
                                if point == max_point:
                                    num_max += 1
                                    curr_players[i].status = 'Won'
                                    winer.append(curr_players[i])
                                else:
                                    curr_players[i].status = 'Lost'
                            for player in winer:
                                player.balance += total_bet / num_max
                        elif num_bust == num_player:
                            for player in curr_players:
                                player.status = 'Draw'
                                player.balance += total_bet / num_player

                    clear_output()
                    Welcome.welcome()
                    mydesk.show_desk()

                    for player in curr_players:
                        player.cards = []
                        if player.status != 'Left':
                            player.status = 'Playing'

                    again_menu = Menu('Next round?', ['Yes, play next round', 'No, leave the table'])
                    again_menu.show_menu()
                    again_option = UserInput.int_input(0, again_menu.menu_length() - 1)

                    if again_option == 0:
                        all_stay = True
                        break
                    elif again_option == 1:
                        all_stay = True
                        player_quit = True
                        break

            elif bet_option == 1:
                print('Leaving the table...')
                time.sleep(1)
                player_quit = True
                break
