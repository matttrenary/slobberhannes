# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:00:47 2020

@author: trenary
"""

import random

def write_file(deck, hand, start, end):
    myfile = open(hand + '.txt', 'w')
    for card in deck[start:end]:
        myfile.write(card)
        myfile.write('\n')
    myfile.close()

deck = ['Ace of Spades',
 'Ace of Hearts',
 'Ace of Clubs',
 'Ace of Diamonds',
 'King of Spades',
 'King of Hearts',
 'King of Clubs',
 'King of Diamonds',
 'Queen of Spades',
 'Queen of Hearts',
 'Queen of Clubs',
 'Queen of Diamonds',
 'Jack of Spades',
 'Jack of Hearts',
 'Jack of Clubs',
 'Jack of Diamonds',
 'Ten of Spades',
 'Ten of Hearts',
 'Ten of Clubs',
 'Ten of Diamonds',
 'Nine of Spades',
 'Nine of Hearts',
 'Nine of Clubs',
 'Nine of Diamonds',
 'Eight of Spades',
 'Eight of Hearts',
 'Eight of Clubs',
 'Eight of Diamonds',
 'Seven of Spades',
 'Seven of Hearts',
 'Seven of Clubs',
 'Seven of Diamonds']

random.shuffle(deck)

hands = ['Rubes','Karl','Mouse','Trenary']
random.shuffle(hands)

write_file(deck, hands[0], 0, 8)
write_file(deck, hands[1], 8, 16)
write_file(deck, hands[2], 16, 24)
write_file(deck, hands[3], 24, 32)
