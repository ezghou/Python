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












