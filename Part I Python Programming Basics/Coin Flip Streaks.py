import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list = []

    for i in range(100):
        coin = random.randint(0,1)

        if coin == 0:
            list.append('H')
        else:
            list.append('T')

#    print(list)
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streakH = 0
    streakT = 0
    for i in range(len(list)-1):
        current = 'H'
        if list[i] == current:
            streakH += 1
            if streakH == 6:
                break
        else:
            streakH = 0

    for i in range(len(list)-1):
        current = 'H'
        if list[i] == current:
            streakH += 1
            if streakH == 6:
                break
        else:
            streakH = 0

    numberOfStreaks += 1
print(numberOfStreaks)
print('Chance of streak: %s%%' % ((numberOfStreaks / 100000) * 100))











