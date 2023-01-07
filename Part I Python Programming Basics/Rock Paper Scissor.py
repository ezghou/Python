import random

print('Rock, Paper, Scissors!')
print()
win = 0
loss = 0
tie = 0

while True:
    print(str(win) + ' Wins,' + str(loss) +  ' Losses, ' +str(tie) + ' Ties')
    print()
    print('Enter your move:  (r)ock (p)aper (s)cissors or (q)uit')
    guess = input()

    if guess == 'p':
        print('Paper versus ...')
    elif guess == 'r':
        print('Rock versus ...')
    elif guess == 's':
        print('Scissors versus ...')
    else:
        break


    chosen = random.randint(1,3)
    comp =''

    if chosen == 1:
        comp = 'Rock'
        print(comp)
        if guess == 'p':
            print('You beat me!')
            win += 1
        elif guess == 'r':
            print('DRAW!')
            tie += 1
        else:
            print('Nah, I win!')
            loss += 1

    elif chosen == 2:
        comp = 'Paper'
        print(comp)
        if guess == 's':
            print('You beat me!')
            win += 1
        elif guess == 'p':
            print('DRAW!')
            tie += 1
        else:
            print('Nah, I win!')
            loss += 1

    else:
        comp = 'Scissors'
        print(comp)
        if guess == 'r':
            print('You beat me!')
            win += 1
        elif guess == 's':
            print('DRAW!')
            tie += 1
        else:
            print('Nah, I win!')
            loss += 1





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






