# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:06:36 2013

@author: yuege
"""

class Card:
    suitList = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rankList = ['narf', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return (self.rankList[self.rank] + " Of " + self.suitList[self.suit])
    
    def __cmp__(self, other):
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        return 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(14):
                self.cards.append(Card(suit,  rank))
    def printDeck(self):
        for card in self.cards:
            print card
    
    def __str__(self):
        s = ''
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + '\n' 
        return s

    def shuffle(self):
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
#            tmp = self.cards[i]
#            self.cards[i] = self.cards[j]
#            self.cards[j] = tmp

    def removeCard(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def popCard(self):
        return self.cards.pop()
        
    def isEmpty(self):
        return (len(self.cards) == 0)
    
    def deal(self, hands, nCards = 999):
        nHands = len(hands)
        for i in range(nCards):
            if self.isEmpty():
                break
            card = self.popCard()
            hand = hands[i % nHands]
            hand.addCard(card)
            
class Hand(Deck):
    def __init__(self, name = ''):
        self.cards = []
        self.name = name
        
    def addCard(self, card):
        self.cards.append(card)
    
    def __str__(self):
        s = 'Hand' + self.name
        if self.isEmpty():
            return s + ' is empty\n'
        else:
            return s + ' contains\n' + Deck.__str__(self)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):
    def removeMatches(self):
        count = 0
        originalCards = self.cards[:]
        for card in originalCards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print 'Hand  %s: %s matches %s' % (self.name,card,match)
                count += 1
        return count
        
class OldMaidGame(CardGame):    
    def play(self, names):
        # remove Queen of Clubs
        self.deck.removeCard(Card(0,12))
        
        # make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
        
        # deal the cards
        self.deck.deal(self.hands)
        print '---------- Cards have been dealt'
        self.printHands()
        
        # remove initial matches
        matches = self.removeAllMatches()
        print '---------- Matches discarded, play negins'
        self.printHands()
        # play until all 50 cars are mathced
        turn = 0
        numHands = len(self.hands)
        while matches < 25:
            matches =  matches + self.playOneTurn(turn)
            turn = (turn + 1) % numHands
        
        print '---------- Game is Over'
        self.printHands()
        
    def removeAllMatches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.removeMatches()
        return count
    
    def printHands(self):
        for hand in self.hands:
            hand.printDeck()
    
    def playOneTurn(self, i):
        if self.hands[i].isEmpty():
            return 0
        neighbor = self.findNeighbor(i)
        pickedCard = self.hands[neighbor]
        self.hands[i].addCard(pickedCard)
        print 'Hand', self.hands[i].name, 'pciked', pickedCard
        count = self.hands[i].removeMatches()
        self.hands[i].shuffle()
        return count
    
    def findNeighbor(self, i):
        numHands= len(self.hands)
        for next in range(1, numHands):
            neighbor = (i + next) % numHands
            if not self.hands[neighbor].isEmpty():
                return neighbor
        
        
























           