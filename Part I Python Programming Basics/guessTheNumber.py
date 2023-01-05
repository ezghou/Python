# Write your code here :-)

import random

print('I am thinking of a number between 1 to 20.')
print('Take a guess.')

count = 0

while True:
    number = str(random.randint(1,20))
    print(str(number) +' '+ str(count))
    guess = input()

    count += 1

    if guess == number:
        print('Good job! You guesssed my number in ' + str(count) + ' guess/es.')
        break

    elif guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        print('That is not a number.')


    if count > 7:
        print('My number was ' + guess +'.')
        break






