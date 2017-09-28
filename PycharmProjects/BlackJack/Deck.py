import random

class Deck(object):
    def __init__(self):
        self.cards = []

    def new_deck(self):
        symbols = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        cards = []

        for x in symbols:
            cards.append([x, u'\u2665'])
            cards.append([x, u'\u2666'])
            cards.append([x, u'\u2660'])
            cards.append([x, u'\u2663'])

        random.shuffle(cards)
        self.cards = cards

    def draw2(self):
        return [self.cards.pop(), self.cards.pop()]

    def draw1(self):
        return self.cards.pop()
