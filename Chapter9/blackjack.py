# blackjack.py
# Simulation Black Jack for Dealer

'''
    Input: The program prompts for and gets the number of games
     to be simulated.
    Output: The program prints out the probability that the dealer
     gets busted.
'''
from random import random, randrange
import time

def main():
    printIntro()
    n = getInput()
    busted = simNGames(n)
    printOutput(busted, n)

def printIntro():
    print('This program simulates the n number of black jack games.' \
          ' And prints out the probability that the dealer gets busted.')

def getInput():
    # Returns the n number of games to be simulated
    n = int(input('How many games to be simulate? '))
    return n

def simNGames(n):
    # Simulates the n number of black jack games.
    # Returns the probability that the dealer gets busted
    bustedList = []
    for total in range(1,11):
        busted = 0
        for i in range(n):
            getBusted = simOneGame()
            if getBusted:
                busted += 1
        bustedList = bustedList.append(busted)

def simOneGame():
    # Simulates one black jack game
    # Return True if the dealer gets busted, otherwise False
    total = 0
    hasAce = False
    while not isEnough(total, hasAce):
        card = dealCard()
        hasAce = checkAce(card)
        total += card
    if total > 21:
        getBusted = True
    else:
        getBusted = False
    return getBusted

def dealCard():
    # Deal a card for dealer
    # Return a value of the card (1-10)
    x = randrange(1,14)
    if x > 10:
        card = 10
    else:
        card = x
    return card

def checkAce(card):
    # Return True if a card is Ace, otherwise False
    if card == 1:
        hasAce = True
    else: hasAce = False
    return hasAce

def isEnough(total, hasAce):
    # Check total is enough 17 or not
    # if hasAce is True, add 10 if the result is over 17, otherwise not
    # Return True if total > 17, otherwise False
    if hasAce and 7 <= total <= 11:
        total += 10
    if total >= 17:
        return True
    else: return False

def printOutput(busted, n):
    print('Your probability of busted is {:.1%}.'.format(busted/n))

if __name__ == '__main__':
    startTime = time.time()
    main()
    print('{:.5f}'.format(time.time() - startTime))
