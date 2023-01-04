# Write your code here :-)


#Rough POS

print('Welcome To Elizabeth Store!')

print('What is your name?')
name = input();
print()
print('Hello, ' + name + '. What I can help you with?')


print('1. Buy')
print('2. Inquire')
print('3. Credit')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue

    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()

    if password == 'swordfish':
        break

print('Access granted')



print('Thank you')


