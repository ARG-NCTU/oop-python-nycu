import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def change(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)   

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def show_hand(self):
        for card in self.hand:
            print(f"{card.rank} of {card.suit}")
    
    def play_card(self):
        print(f"{self.name}, it's your turn.")
        print("Choose a card to play:")
        for i, card in enumerate(self.hand):
            print(f"{i+1}. {card.rank} of {card.suit}")
        choice = int(input("Enter the number of the card you want to play: ")) - 1
        return self.hand.pop(choice)
    
    def reorganize_hand(self):
        self.hand.sort(key=lambda x:(x.suit,x.rank))


def computer_play_card(center, cp):
    valid_cards = []
    for card in cp.hand:
        if card.rank > center.rank or (card.rank == center.rank and card.suit > center.suit):
            valid_cards.append(card)
    if valid_cards:
        cp_card = random.choice(valid_cards)
        cp.hand.remove(cp_card)
        return cp_card
    else:
        return "pass"


# Example usage
deck = Deck()
deck.shuffle()
center = Card("Clubs", "3")
cp = [None, None, None]

player = Player("Player")
cp[0] = Player("Computer 1")
cp[1] = Player("Computer 2")
cp[2] = Player("Computer 3")
for i in range(13):
        player.draw(deck)
for P in cp:
    for i in range(13):
        P.draw(deck)

player.reorganize_hand()
#player.play_card()

for P in cp:
    center=computer_play_card(center, P)
    print(center)


