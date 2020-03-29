import os
import time

coins = ['Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø','Ø']
Player = 1
GameOver = False

def show_coins():
    os.system('cls')
    global coins
    print('')
    print(coins)
    print('')

def switch_player():
    global Player
    if Player == 1:
        Player = 2
    else:
        Player = 1

def pause():
    print('Press Enter to exit ', end = '')
    end = input()

print("""============================= DR NIM =============================
      Rules: Players will take turns choosing how many marbles
             they want to remove, each player can remove upto 3
             marbles but not more than 3, the player that removes
             the last marble wins the game.\n""")

print("""Choose your opponent:
         [a] Another Player
         [b] Dr NIM\n""")

print('Your opponent: ', end = '')
opponent = str(input()).lower()
if opponent != 'a' and opponent != 'b':
    while opponent != 'a' and opponent != 'b':
        print('Invalid input please try again: ', end = '')
        opponent = str(input())
numcoins = 0

if opponent == 'a':

    while GameOver == False:
        show_coins()
        print('Player' + str(Player) + ' enter the number of coins to remove: ', end = '')
        numcoins = int(input())
        if numcoins > 3 or numcoins <= 0 or numcoins > len(coins):
            while numcoins > 3 or numcoins <= 0 or numcoins > len(coins):
                print('Invalid input please try again: ', end = '')
                numcoins = int(input())
        for i in range(numcoins):
            coins.remove('Ø')

        if len(coins) == 0:
            print('\nPlayer'+str(Player) + ' wins\n')
            pause()
            GameOver = True
        else:
            switch_player()

if opponent == 'b':
    
    while GameOver == False:
        
            show_coins()
            print('Player'+str(Player) + ' enter the number of coins to remove: ', end = '')
            numcoins = int(input())
            if numcoins > 3 or numcoins <= 0:
                while numcoins > 3 or numcoind <= 0:
                    print('Invalid input please try again: ', end = '')
                    numcoins = int(input())
            for i in range(numcoins):
                coins.remove('Ø')

            if len(coins) == 0:
                if Player == 1:
                    print('\nYou win.\n')
                    pause()
                    GameOver = True
                elif Player == 2:
                    print('\n\nDr NIM wins.\n')
                    pause()
                    GameOver = True
            else:
                switch_player()
                show_coins()
                print("""\n Dr Nim is making its move.""", end = '')
                time.sleep(2)
                for i in range(4-numcoins):
                    coins.remove('Ø')

                if len(coins) == 0:
                    if Player == 1:
                        print('\nYou win.\n')
                        pause()
                        GameOver = True
                    elif Player == 2:
                        print('\n\nDr NIM wins.\n')
                        pause()
                        GameOver = True
                    else:
                        switch_player()
