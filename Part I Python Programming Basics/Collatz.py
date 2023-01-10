def collatz(number):
    if number == 1:
        return number
    if number % 2 == 0:
        ans = number // 2
        return ans

    else:
        answer = 3 * number + 1
        return answer

try:

    while True:
        print('Enter a number (Enter "000" to quit): ', end = '')
        guess = int(input())

        if guess == 000:
            break

        while True:
            guess = collatz(guess)
            print(guess)
            if guess == 1:
                break



except:
    print('Enter a valid number!')










