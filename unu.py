import random

colors = ("red", "yellow", "green", "blue")


class Card:
    def __init__(self, num, color):
        self.num = num
        self.color = color

    def print_card(self):
        print(self.num, self.color)


def generate_hand(card_num):
    h = []
    for x in range(card_num):
        color = random.choice(colors)
        num = random.randint(1, 8)
        h.append(Card(num, color))
    return h


def show_hand(h):
    for x in h:
        x.print_card()


hand = generate_hand(8)
show_hand(hand)