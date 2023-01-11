
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

#for i in range(len(myDogs)):
#    print('Index ' + str(i) + ' is dog ' + myDogs[i] )

for index, name in enumerate(myDogs):
    print(' Index ' + str(index) + ' is dog ' + name )



def eggs(someParameters):
    someParameters.append("heyo")

spam = [1,2,3]
eggs(spam)

print(spam)

