import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split() 

class Deck:
    """
    
    """
    cardsNumber = 52
    cards=list()

    def __init__(self):
        for sign in SUITE:
            for rank in RANKS:
                self.cards.append(sign+rank)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def split(self):
        length = len(self.cards)
        middle = length//2
        return self.cards[:middle], self.cards[middle:]

class Hand:

    def __init__(self, cards):
        self.cards = cards
    
    def addCard(self, card):
        self.cards.append(card)
    
    def addCards(self, stack):
        for card in stack:
            self.cards.append(card)
    
    def removeCard(self, card):
        self.cards.remove(card)
    
    def removeCards(self, stack):
        for card in stack:
            self.cards.remove(card)

class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def drawCard(self):
        return self.hand.cards[0]

    def drawMultiple(self,no):
        return self.hand.cards[:no]

    def hasCards(self):
        if not self.hand.cards:
            return False
        return True

myDeck = Deck()
myDeck.shuffle()
list1,list2 = myDeck.split()
hand1 = Hand(list1)
hand2 = Hand(list2)

print("Welcome to War, let's begin...")
namePlayer1=input("Player one, enter your name:")
namePlayer2=input("Player two, enter your name:")

Player1 = Player(namePlayer1,hand1)
Player2 = Player(namePlayer2,hand2)

while True:
    card1 = Player1.drawCard()
    card2 = Player2.drawCard()
    number1 = card1[1:]
    number2 = card2[1:]
    if number1 == "10":
        number1 = "A"
    if number2 == "10":
        number2 = "A"
        
    if number1 > number2 :
        print(card2)
        Player1.hand.addCard(card2)
        Player2.hand.removeCard(card2)
    elif number1==number2:
        if len(Player1.hand.cards) < 4:
            number = len(Player1.hand.cards)
            stack1 = Player1.drawMultiple(number)
            stack2 = Player2.drawMultiple(number)
        elif len(Player2.hand.cards) < 4:
            number = len(Player2.hand.cards)
            stack1 = Player1.drawMultiple(number)
            stack2 = Player2.drawMultiple(number)
        else:
            stack1 = Player1.drawMultiple(4)
            stack2 = Player2.drawMultiple(4)

        print("STACK PLAYER 1 : {}".format(stack1))
        print("STACK PLAYER 2 : {}".format(stack2))
        card1 = stack1[-1]
        card2 = stack2[-2]
        number1 = stack1[1:]
        number2 = stack2[1:]
        if number1 == "10":
            number1 = "A"
        if number2 == "10":
            number2 = "A"
        if number1 > number2:
            Player1.hand.addCards(stack2)
            Player2.hand.removeCards(stack2)
        else:
            Player2.hand.addCards(stack1)
            Player1.hand.removeCards(stack1)
        
    else:
        print(card1)
        Player2.hand.addCard(card1)
        Player1.hand.removeCard(card1)
    
    if len(Player1.hand.cards) == 0:
        print("{} has won!".format(Player1.name))
        break
    elif len(Player2.hand.cards) == 0:
        print("{} has won!".format(Player2.name))
        break