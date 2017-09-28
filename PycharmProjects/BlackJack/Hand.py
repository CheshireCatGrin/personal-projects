class Hand(object):
    def __init__(self):
        self.cards = []

    def hit(self, card):
        self.cards += card

    def deal(self, cardlist):
        self.cards = cardlist

    def compute_score(self):
        if self.counter() == 21:
            return "BlackJack"
        elif self.counter() > 21:
            return "Bust"
        else:
            return self.counter()

    def counter(self):
        counter = 0
        for x in self.cards:
            if type(x[0]) == int:
                counter += x[0]
            else:
                if x[0] == 'J' or x[0] == 'Q' or x[0] == 'K':
                    counter += 10
                else:
                    counter += 11

        if "A" in [x[0] for x in self.cards] and counter > 21:
            counter -= 10
        return counter

    def printdealer(self):
        d0 = "Dealer's cards:"
        d1 = ' _______ '
        if self.cards[0][0] == 10:
            d2 = '|' + str(self.cards[0][0]) + '   ' + str(self.cards[0][1]) + ' |'
        else:
            d2 = '| ' + str(self.cards[0][0]) + '   ' + str(self.cards[0][1]) + ' |'
        d3 = '|       |'
        d4 = '|   ' + str(self.cards[0][1]) + '   |'
        d5 = '|       |'
        if self.cards[0][0] == 10:
            d6 = '| ' + str(self.cards[0][1]) + '   ' + str(self.cards[0][0]) + '|'
        else:
            d6 = '| ' + str(self.cards[0][1]) + '   ' + str(self.cards[0][0]) + ' |'
        d7 = "'-------'"

        for x in range(len(self.cards) - 1):
            printlist = [d0, d1 + ' _______ ', d2 + '|       |', d3 + '|       |', d4 + '|       |', d5 + '|       |',
                         d6 + '|       |', d7 + "'-------'"]
        for d in printlist:
            print(d)
        print()
        print()

    def printdealerreveal(self):
        l0 = "Dealer's hand is..."
        l1 = ''
        l2 = ''
        l3 = ''
        l4 = ''
        l5 = ''
        l6 = ''
        l7 = ''
        for x in self.cards:
            l1 = ' _______ ' + l1
            if x[0] == 10:
                l2 = '|' + str(x[0]) + '   ' + str(x[1]) + ' |' + l2
            else:
                l2 = '| ' + str(x[0]) + '   ' + str(x[1]) + ' |' + l2
            l3 = '|       |' + l3
            l4 = '|   ' + str(x[1]) + '   |' + l4
            l5 = '|       |' + l5
            if x[0] == 10:
                l6 = '| ' + str(x[1]) + '   ' + str(x[0]) + '|' + l6
            else:
                l6 = '| ' + str(x[1]) + '   ' + str(x[0]) + ' |' + l6
            l7 = "'-------'" + l7
        for l in [l0, l1, l2, l3, l4, l5, l6, l7]:
            print(l)