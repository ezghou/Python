
myDogs = ['','','']
count = 0
while True:
    print('Enter name of your dog:', end = '')

    myDogs[count] = input()
    print(myDogs)
    count += 1
    if count > 2:
        break

print(myDogs)

