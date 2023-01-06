import random

print('Let us play Rock, Paper, Scissors!')


while True:
    chosen = random.randint(1,3)
    print(chosen)
    comp =''
    guess = input()

    if chosen == 1:
        comp = 'Rock'
        print(comp + ' vs. ' + guess)
        if guess == 'Paper':
            print('You beat me!')
        elif guess == comp:
            print('DRAW!')
        else:
            print('Nah, I win!')

    elif chosen == 2:
        comp = 'Paper'
        print(comp + ' vs. ' + guess)
        if guess == 'Scissors':
            print('You beat me!')
        elif guess == comp:
            print('DRAW!')
        else:
            print('Nah, I win!')

    else:
        comp = 'Scissors'
        print(comp + ' vs. ' + guess)
        if guess == 'Rock':
            print('You beat me!')
        elif guess == comp:
            print('DRAW!')
        else:
            print('Nah, I win!')

    break










