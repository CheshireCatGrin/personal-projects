from Hand import Hand
from Player import Player
from Deck import Deck

def main():

    def yes_or_no(input):
        if input in ['yes', 'Yes', 'Yeah', 'yeah', "Sure", 'sure']:
            return True
        elif input in ['No', 'no', 'Nope', 'nope']:
            return False
        else:
            return None

    def cycle_player(nplayers, current_player): # returns the next player, p + 1, in the list of players, or else returns player to 0
        if nplayers == current_player + 1:
            return 0
        else:
            return current_player + 1

    def print_players(playerlist):
        l0, l1, l2, l3, l4, l5, l6, l7, l8 = ['', '', '', '', '', '', '', '', '']
        for p in playerlist:
            l0 = l0 + p.name + "'s hand:"
            for x in p.hand.cards:
                l1 = l1 + ' _______ '
                if x[0] == 10:
                    l2 = l2 + '|' + str(x[0]) + '   ' + str(x[1]) + ' |'
                else:
                    l2 = l2 + '| ' + str(x[0]) + '   ' + str(x[1]) + ' |'
                l3 = l3 + '|       |'
                l4 = l4 + '|   ' + str(x[1]) + '   |'
                l5 = l5 + '|       |'
                if x[0] == 10:
                    l6 = l6 + '| ' + str(x[1]) + '   ' + str(x[0]) + '|'
                else:
                    l6 = l6 + '| ' + str(x[1]) + '   ' + str(x[0]) + ' |'
                l7 = l7 + "'-------'"
            l8 = l8 + "Card Total: " + str(p.hand.compute_score())
            printlist = [l0, l1, l2, l3, l4, l5, l6, l7, l8]
            start = len(l2) + 10
            for e in range(len(printlist)):
                printlist[e] = printlist[e] + (" " * (start - len(printlist[e])))
            l0, l1, l2, l3, l4, l5, l6, l7, l8 = printlist
        for l in [l0, l1, l2, l3, l4, l5, l6, l7, l8]:
            print(l)

    def print_rules():
        print()
        print("-" * 50)
        print(" " * 22 + "Rules")
        print("-" * 50)
        print()
        print()
        print("In BlackJack, it is you versus the dealer. The dealer deals you and himself two cards each from the ")
        print("deck. After the deal, you must count the points in your hand. All face-cards are worth 10, and the ")
        print("ace is worth either 1 or 11, whichever benefits you most. The rest of the cards are worth their ")
        print('stated numbers.')
        print()
        print('The dealer will then "hit" which means to take an extra card from the deck until he has either 17 ')
        print('points or more. Then, he will "stand". ' + "Afterwords, it is the players' turn to hit or stand.")
        print()
        print("Here is the kicker: the dealer will only show you his first drawn card, and the rest will be ")
        print('facedown. You on the other hand must always keep your cards faceup, significantly')
        print('disadvantaging you. But hey, you know the saying: the house always wins.')
        print()
        print("You start with 1000 dollars with which to bet. If you draw with the dealer, nothing happens. If you ")
        print("win, then you receive double your bet. If you lose, the dealer receives double your bet.")
        print()
        print("That's it. My creator was too lazy to build a split-function, so this is a simplified version ")
        print("of Blackjack. Have fun!")
        print()

    print("-" * 50)
    print(" " * 20 + "BlackJack")
    print("-" * 50)
    print()

    print()
    print("Welcome to Jordan's BlackJack program!")
    print("Would you like to hear the rules?")

    reply = input(">>> ")
    while yes_or_no(reply) == None:
        print("I'm sorry. I only understand 'yes' or 'no' replies. Try again?")
        reply = input(">>> ")

    if yes_or_no(reply):
        print_rules()

    print("How many players are playing?")
    while True:
        nplayers = input(">>>  ")
        try:
            nplayers = int(nplayers)
        except:
            print("Please enter a valid integer value between 1 and 4.")
            continue

        if 0 < nplayers < 5:
            break
        else:
            print("Please enter a valid integer value between 1 and 4.")
            continue

    dealer_hand = Hand()
    handlist = [Hand() for x in range(nplayers)]

    namelist = []
    for x in range(nplayers):
        print("Player " + str(x+1) + ", what is your name?")
        namelist.append(input(">>>   "))
        print()

    playerlist = [Player(namelist[x], x + 1, handlist[x]) for x in range(nplayers)]
    current_deck = Deck()

    while True:
        # This portion of the loop will reset all hands (from previous rounds), reset the turn counter to 0, and
        # create a fresh deck. It will then ask for bets from players, and then deal them cards from the deck.

        current_deck.new_deck()

        for player in playerlist:
            player.place_bet()

        dealer_hand.deal(current_deck.draw2())

        for x in handlist:
            x.deal(current_deck.draw2())

        turn_counter = 0

        print()
        print('Dealing...')
        print()

        while True:
            # This while loop lets players hit or stand. It will also print the current hands.
            # It will break when the dealer and player have either stood or else reached bust / blackjack.

            current_player = playerlist[turn_counter]
            current_hand = current_player.hand

            while dealer_hand.counter() < 17:
                dealer_hand.cards.append(current_deck.draw1())
            dealer_hand.printdealer()

            print_players(playerlist)
            print()

            if current_hand.compute_score() == "BlackJack":
                turn_counter = cycle_player(nplayers, turn_counter)
                if turn_counter == 0:
                    break
                else:
                    continue

            elif current_hand.compute_score() == "Bust":
                turn_counter = cycle_player(nplayers, turn_counter)
                if turn_counter == 0:
                    break
                else:
                    continue

            else:
                move = input(str(current_player.name) + ", hit or stand?  >>> ")

                while move not in ['hit', 'Hit', 'stand', 'Stand']:
                    print("Please choose either hit or stand.")
                    move = input("Hit or Stand?  >>> ")

                if move in ['hit', 'Hit']:
                    current_hand.cards.append(current_deck.draw1())
                    continue
                elif move in ['stand', 'Stand']:
                    turn_counter = cycle_player(nplayers, turn_counter)
                    if turn_counter == 0:
                        break
                    else:
                        continue

        # This portion of the loop will reveal the dealer's hand, tell the players the outcome, update their banks
        # and ask the players if they would like another round.
        dealer_hand.printdealerreveal()
        if dealer_hand.compute_score == "BlackJack":
            print("Dealer got BlackJack!")
        elif dealer_hand.compute_score == "Bust":
            print('Dealer went bust!')
        else:
            print('Dealer got ' + str(dealer_hand.compute_score()) + "!")
        print()

        for x in range(len(playerlist)):

            if playerlist[x].hand.compute_score() == dealer_hand.compute_score():
                print(playerlist[x].name + ", you draw. You get your bet of " + str(playerlist[x].bet) + ' back.')
                continue
            else:
                if playerlist[x].hand.compute_score() == "BlackJack" or dealer_hand.compute_score() == "Bust":
                    print(playerlist[x].name + ", you beat the dealer!. You gained " + str(playerlist[x].bet) + "!")
                    playerlist[x].update_bank(playerlist[x].bet)
                    continue

                elif dealer_hand.compute_score() == "BlackJack" or playerlist[x].hand.compute_score() == "Bust":
                    print(playerlist[x].name + ", you lost " + str(playerlist[x].bet) + "!")
                    playerlist[x].update_bank(-1 * playerlist[x].bet)
                    continue

                else:
                    if playerlist[x].hand.compute_score() > dealer_hand.compute_score():
                        print(playerlist[x].name + ", you beat the dealer!. You gained " + str(playerlist[x].bet) + "!")
                        playerlist[x].update_bank(playerlist[x].bet)
                        continue
                    else:
                        print(playerlist[x].name + ", you lost " + str(playerlist[x].bet) + "!")
                        playerlist[x].update_bank(-1 * playerlist[x].bet)
                        continue
        print()
        for x in range(len(playerlist)):
            print(playerlist[x].name + "'s bank: " + str(playerlist[x].bank))
        print()

        print("Would you like to play another round?")
        answer = input(">>>  ")

        while yes_or_no(answer) == None:
            print("I'm sorry. I do not understand. Please enter yes or no.")
            answer = input(">>>  ")
        if yes_or_no(answer):
            continue
        else:
            print("Thanks for playing!")
            break

main()