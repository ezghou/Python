
myDogs = []
while True:
    print('Enter name of your dog (enter 0 to end):', end = '')

    dog = input()

    if dog == '0':
        break

    myDogs = myDogs + [dog] #List Concatenation
    print(myDogs)


print()
print('The dog names are:')
for name in myDogs:
    print(' ' + name)

