import random


class Card:
    """the class object for the unu game"""
    def __init__(self, num, color):
        """initiate the card"""
        self.num = num
        self.color = color

    def print_card(self):
        """print the card"""
        print(self.num, self.color)
        
    def is_same(self, other_card):
        """returns true if both aspects of the card are the same"""
        return self.num == other_card.num and self.color == other_card.color

    def is_equal(self, other_card):
        """returns true if the cards have one similar aspect"""
        return self.num == other_card.num or self.color == other_card.color

    def text(self):
        """returns a string version of the card values"""
        return "%s %s" % (self.num, self.color)


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


def string_to_card(stri):
    """turns a string into a card obj"""
    x = stri.split(" ")
    return Card(int(x[0]), x[1])


def exist_in_hand(h, c):
    for x in h:
        if x.is_same(c):
            return True
    return False


def get_card():
    print("The center card is:", centercard.text(), "your deck is:")
    show_hand(you)
    played = input("what do you want to play: ")
    played = string_to_card(played)
    if played.is_equal(centercard) and exist_in_hand(you, played):
        return played
    elif played.is_equal(centercard) and not exist_in_hand(you, played):
        print('''choose a card from your hand!
        try again''')
        return get_card()


colors = ("red", "yellow", "green", "blue")
win = False
centercard = Card(random.randint(1, 8), random.choice(colors))

enemy = generate_hand(8)
you = generate_hand(8)


