"""
Take home lab

A game of gambling and dice rolling with the following rules:
Two dice are rolled
You start with $100 and bet $10 on each play
Running out of money is a loss
On the first roll, a total of 7 or 11 is an automatic win
On the first roll, a total of 2, 3, or 12 is an automatic loss
Any other number is called "the Point" and means you must roll again
On the next rolls:
-A 7 is a loss
-Rolling the same point number again is a win
-Any other number is a point number and you roll again

"""
from random import randrange

def roll():
    return(randrange(1,13))

def wincondition(finalrolls, balance):
    print('Congratulations! You win!\n',
            'You rolled {}! Ending balance {}'.format(finalrolls, balance))

def losscondition(finalrolls, balance):
    print('Bah! You lost!\n',
          'You rolled {}. Ending balance ${}'.format(finalrolls, balance))

playing = True
balance = 100

while playing!=False:
    start = input("Welcome to the Dice Game! Type anything to continue or quit to quit.")
    rolls = []
    
    if start=='quit':
        break
    else:

        #firstroll
        firstroll = roll()
        rolls.append(firstroll)
        balance = balance - 10 

        if balance<=0:
            print("You ran out of money!")
            playing = False
        elif firstroll==7 or firstroll==11:
            balance+=20
            wincondition(rolls, balance)
        elif firstroll==2 or firstroll==3 or firstroll==12:
            losscondition(rolls, balance)
        else:
            print('You rolled a {} so you get to roll again!'.format(firstroll))
            #further rolls
            point = True
            prevroll = 0
            while point!=False:
                nextroll = roll()
                rolls.append(nextroll)
                if nextroll==prevroll:
                    balance+=20
                    wincondition(rolls, balance)
                    prevroll = nextroll
                    point = False
                elif nextroll==7:
                    losscondition(rolls, balance)
                    prevroll = nextroll
                    point = False
                else:
                    print('You rolled a {} so you get to roll again!'
                          .format(nextroll))
                    prevroll = nextroll
