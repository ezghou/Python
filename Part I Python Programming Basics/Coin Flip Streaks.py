import random

numberOfStreaks = 0

for experimentNumber in range(10):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list = []

    for i in range(5):
        coin = random.randint(0,1)

        if coin == 0:
            list.append('H')
        else:
            list.append('T')

    print(list)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streakH = 0
    streakT = 0
    for i in range(len(list)-1):
            if list[i] == list[i+1]:
                streakH += 1


    print(streakH)


print('Chance of streak: %s%%' % (numberOfStreaks / 100))











