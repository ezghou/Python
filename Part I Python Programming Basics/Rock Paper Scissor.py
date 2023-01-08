import random, sys

win = 0
loss = 0
tie = 0

def printIntro(win,loss,tie):
    print('Rock, Paper, Scissors!')
    print()
    print(str(win) + ' Wins,' + str(loss) +  ' Losses, ' +str(tie) + ' Ties')
    print()
    print('Enter your move:  (r)ock (p)aper (s)cissors or (q)uit')

def iWin():

    print()
    print('Nah, I win!')
    print()
    print()
    global loss
    loss += 1

def youBeatMe():
    print()
    print('You beat me!')
    print()
    print()
    global win
    win += 1

def draw():
    print()
    print('DRAW!')
    print()
    print()
    global tie
    tie += 1

while True:
    printIntro(win,loss,tie)

    guess = input()

    if guess == 'p':
        print('Paper versus ...')
    elif guess == 'r':
        print('Rock versus ...')
    elif guess == 's':
        print('Scissors versus ...')
    else:
        sys.exit()


    chosen = random.randint(1,3)
    comp =''

    if chosen == 1:
        comp = 'Rock'
        print(comp)
        if guess == 'p':
            youBeatMe()
        elif guess == 'r':
            draw()
        else:
            iWin()

    elif chosen == 2:
        comp = 'Paper'
        print(comp)
        if guess == 's':
            youBeatMe()
        elif guess == 'p':
            draw()
        else:
            iWin()

    else:
        comp = 'Scissors'
        print(comp)
        if guess == 'r':
            youBeatMe()
        elif guess == 's':
           draw()
        else:
            iWin()





#print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
#wins = 0
#losses = 0
#ties = 0

#while True: # The main game loop.
#    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#    while True: # The player input loop.
#        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#        playerMove = input()
#        if playerMove == 'q':
#            sys.exit() # Quit the program.
#        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#            break # Break out of the player input loop.
#        print('Type one of r, p, s, or q.')#

    # Display what the player chose:
#    if playerMove == 'r':
#        print('ROCK versus...')
#    elif playerMove == 'p':
#        print('PAPER versus...')
#    elif playerMove == 's':
#        print('SCISSORS versus...')

    # Display what the computer chose:
#    randomNumber = random.randint(1, 3)
#    if randomNumber == 1:
#        computerMove = 'r'
#        print('ROCK')
#    elif randomNumber == 2:
#        computerMove = 'p'
#        print('PAPER')
#    elif randomNumber == 3:
#        computerMove = 's'
#        print('SCISSORS')

    # Display and record the win/loss/tie:
#    if playerMove == computerMove:
#        print('It is a tie!')
#        ties = ties + 1
#    elif playerMove == 'r' and computerMove == 's':
#        print('You win!')
#        wins = wins + 1
#    elif playerMove == 'p' and computerMove == 'r':
#        print('You win!')
#        wins = wins + 1
#    elif playerMove == 's' and computerMove == 'p':
#        print('You win!')
#        wins = wins + 1
#    elif playerMove == 'r' and computerMove == 'p':
#        print('You lose!')
#        losses = losses + 1
#    elif playerMove == 'p' and computerMove == 's':
#        print('You lose!')
#        losses = losses + 1
#    elif playerMove == 's' and computerMove == 'r':
#        print('You lose!')
#        losses = losses + 1






