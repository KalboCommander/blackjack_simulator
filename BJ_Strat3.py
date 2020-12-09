from BJ_Objects import *

##Strategy - Player will always hit on soft 18 (Ace-7) when dealers upcard is 9,10, or Ace.
def Hit_Soft_18(games_max,ind):

    player1 = Player("Bob")
    casinodealer = Dealer()

    fresh_deck = Deck()
    fresh_deck.shuffle()
    
    ##Game Counter
    gc = 0

    ##Record counter
    blackjack_players = ['DEALER', 'PLAYER1','PUSH']
    records = {i: 0 for i in blackjack_players}

    ##Blackjack counter
    dealer_bj = 0
    player_bj = 0

    #Player Wallet
    wallet = 1000

    while gc < games_max:

        deal(casinodealer,player1,fresh_deck)

        dealer_sum = evaluate_cards(casinodealer)
        player_sum = evaluate_cards(player1)

        ##Check for Blackjacks - if either has it, automatic win.  If both, push/tie.

        if dealer_sum == 21 and player_sum != 21:
            # print('DEALER HAS BLACKJACK!  YOU LOSE!\n')
            records['DEALER'] += 1
            gc += 1
            dealer_bj += 1
            wallet -= 25
        elif player_sum == 21 and dealer_sum != 21:
            # print('PLAYER1 HAS BLACKJACK!  YOU WIN!\n')
            records['PLAYER1'] += 1
            gc += 1
            player_bj += 1
            wallet += 37.5

        ##Strategy Implementation (lines 49-64)
        else:
            condition_a = player1.hand[0].rank == 'Ace' and player1.hand[1].rank == '7'
            condition_b = player1.hand[0].rank == '7' and player1.hand[1].rank == 'Ace'
            dealer_set = ['9', '10', 'Jack', 'Queen', 'King','Ace']
            
            if (condition_a or condition_b) and (casinodealer.hand[1].rank in dealer_set):
                player1.draw(fresh_deck)
                player_sum = evaluate_cards(player1)
            
            while player_sum < 17:
                player1.draw(fresh_deck)
                player_sum = evaluate_cards(player1) 

            while dealer_sum < 17:
                casinodealer.draw(fresh_deck)
                dealer_sum = evaluate_cards(casinodealer)

            ##check if player busted
            if player_sum > 21:
                records['DEALER'] += 1
                # print('DEALER WIN\n')
                gc += 1
                wallet -= 25
            ##check if dealer busted
            elif dealer_sum > 21:
                records['PLAYER1'] += 1
                # print('PLAYER WIN\n')
                gc += 1  
                wallet += 25
            ##player1 wins by getting closer to 21
            elif player_sum > dealer_sum and player_sum <= 21: 
                records['PLAYER1'] += 1
                # print('PLAYER WIN\n')
                gc += 1
                wallet += 25
            ##dealer wins by getting closer to 21
            elif dealer_sum > player_sum and dealer_sum <= 21:
                records['DEALER'] += 1
                # print('DEALER WIN\n')
                gc += 1
                wallet -= 25
            elif player_sum == dealer_sum:
                records['PUSH'] += 1
                # print('PUSH\n')
                gc += 1       

        # print('***DEALER\'s HAND***')
        # print('Downcard / Upcard')
        # casinodealer.showHand()
        # print('Dealers Current Hand Sum: {}\n'.format(dealer_sum))
        
        # print('***PLAYER\'s HAND***')
        # print('Downcard / Upcard')
        # player1.showHand()
        # print('Player 1 Current Hand Sum: {}'.format(player_sum))

        ##End current game.  Dispose of cards
        casinodealer.disposeHand()
        player1.disposeHand()

        # print('\n')
        # print('Remaining Cards in Deck: {}'.format(fresh_deck.count()))
        # print('\n')
        # print('**************************************************************************************************')
        
        if ind==0:    
            ##Check to see if enough cards for next game.  If not, reshuffle deck.
            if fresh_deck.count() < 12:
                fresh_deck = Deck()
                fresh_deck.shuffle()
                # print('**************************************************************************************************')
                # print('Reshuffling Deck...\n')
                # print('**************************************************************************************************')
        
        if ind==1:
            fresh_deck = Deck()
            fresh_deck.shuffle() 

    win_rate = records['PLAYER1'] / ((records['PLAYER1'] + records['DEALER'])) * 100
    win_rate = truncate(win_rate,decimals=2)

    print('\n*** "Hit on Soft 18" Strategy ***')
    print('\nTotal Games Played: {}'.format(gc))
    print('Final Record: {}'.format(records))
    print('Player1 Win Rate: {}%'.format(win_rate))
    print('Player1 Blackjacks: {}'.format(player_bj))
    print('Dealer Blackjacks: {}'.format(dealer_bj))
    print('Ending Wallet Amount: ${}'.format(wallet))