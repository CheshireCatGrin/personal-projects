class Player(object):
    def __init__(self, name, playernumber, hand, bank=1000, bet=0):
        self.name = name
        self.playernumber = playernumber
        self.hand = hand
        self.bank = bank
        self.bet = bet

    def place_bet(self):
        while True:
            answer = input("Place your bet, " + self.name + ": ")
            try:
                answer = int(answer)
            except:
                print("You must enter an integer value. Try again. ")
                continue
            self.bet = int(answer)
            if self.bet < self.bank:
                break
            else:
                print("You only have " + str(self.bank) + " money in your bank! Try a smaller bet.")
                continue

    def update_bank(self, gainorloss):  # Will update the attribute "bank" by adding the second argument
        self.bank = self.bank + gainorloss  # passed in. Important to enter losses as negative numbers.