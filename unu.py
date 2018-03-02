import random

colors = ("red", "yellow", "green", "blue")


class Card:
    """the class object for the unu game"""
    def __init__(self, num, color):
        """initiate the card"""
        self.num = num
        self.color = color

    def print_card(self):
        """print the card"""
        print(self.num, self.color)


def generate_hand(card_num):
    """returns a list containing a specified amount of cards"""
    h = []
    for x in range(card_num):
        h.append(Card(random.randint(1, 8), random.choice(colors)))
    return h


def show_hand(h):
    """prints a hand"""
    for x in h:
        x.print_card()


hand = generate_hand(8)
show_hand(hand)