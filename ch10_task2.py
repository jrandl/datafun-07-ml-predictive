# Example From 10.12 Named Tuples page 399

from collections import namedtuple

Card = namedtuple('Card', ['face', 'suit'])

card = Card(face='Ace', suit='Spades')

print(card.face)  
print(card.suit) 
print(card) 

values = ['Queen', 'Hearts']

card = Card._make(values)

print(card)

print(card._asdict)