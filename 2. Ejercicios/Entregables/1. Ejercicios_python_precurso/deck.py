#Make a program using while that generates a deck of cards of 4 different suits. The deck must have 40 cards.


import random

suits = ["clubs", "diamonds", "hearts", "spades"]
new_deck = []

while len(new_deck) < 40:
    random_pick = random.choice(suits)
    repeats = 0
    for elem in new_deck:
        if random_pick == elem:
            repeats += 1
    if repeats < 10:
        new_deck.append(random_pick)
    else:
        continue

print(f'New deck variable name : new_deck \nNumber of cards in Deck: {len(new_deck)}\nOrther of cards are:\n{new_deck}')