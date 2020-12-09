import random
import sys

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace'];
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,1]

class Card:
    def __init__(self,rank,val):
        self.rank = rank
        self.value = val
        
    def show(self):
        print("Rank:{}, Value:{}".format(self.rank,self.value))
    
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for x in range(0,len(ranks)):
            for y in range(0,4):
                self.cards.append(Card(ranks[x],values[x]))
                
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def cardDraw(self):
        return self.cards.pop()
    
    def count(self):
        x = 0
        for c in self.cards:
            x+=1
        return x
    
    def show(self):
        for c in self.cards:
            c.show()
            
class Dealer:
    def __init__(self):
        self.hand=[]
    
    def draw(self, deck):
        self.hand.append(deck.cardDraw())
        return self
            
    def showHand(self):
        for card in self.hand:
            card.show()
            
    def disposeHand(self):
        self.hand.clear()

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.cardDraw())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
            
    def disposeHand(self):
        self.hand.clear()

def deal(x,y,z):
    x.draw(z)
    y.draw(z)
    x.draw(z)
    y.draw(z)

def evaluate_cards(U):
    ace_condition1 = U.hand[0].rank == 'Ace' and U.hand[1].rank != 'Ace'
    ace_condition2 = U.hand[1].rank == 'Ace' and U.hand[0].rank != 'Ace'
    ace_condition3 = U.hand[0].rank == 'Ace' and U.hand[1].rank == 'Ace'
    
    if ace_condition1: 
        U.hand[0].value = 11
    if ace_condition2:
        U.hand[1].value = 11
    if ace_condition3:
         U.hand[0].value = 11
         U.hand[1].value = 1
        
    total =  0
    for n in range(len(U.hand)):
        total += U.hand[n].value
    
    if total > 21 and ace_condition1:
        U.hand[0].value = 1
        total =  0
        for n in range(len(U.hand)):
            total += U.hand[n].value
    
    if total> 21 and ace_condition2:
        U.hand[1].value = 1
        total =  0
        for n in range(len(U.hand)):
            total += U.hand[n].value
            
    if total> 21 and ace_condition3:
        U.hand[0].value = 1
        U.hand[1].value = 1
        total =  0
        for n in range(len(U.hand)):
            total += U.hand[n].value
    
    return total

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier