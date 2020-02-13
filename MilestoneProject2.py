import random #used to shuffle the deck prior to dealing

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = [] #empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) 

    def __str__(self):
        deck_comp = " " #Starts with an empty string
        for card in self.deck:
           deck_comp += '\n' + card.__str__() #add each card object's print string
        return "The deck has " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck) #here we shuffle the deck 
    
    def deal(self):
        single_card = self.deck.pop() #takes the last letter from the deck
        return single_card

'''test_deck = Deck()
print(test_deck)
    
'''
# the Hand class may be used to calculate the value of those cards using the values dictionary defined above
class Hand:
    def __init__(self):
        self.cards = [] #empty list
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        pass

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_player.value

for card in test_player.cards:
    print(card)