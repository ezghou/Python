def collatz(number):
    if number % 2 == 0:
        ans = number // 2
        print(ans)
        return ans

    else:
        answer = 3 * number + 1
        print(answer)
        return answer

try:
    print('Enter a number: ', end = '')
    guess = int(input())

    while True:
        if guess == 1:
            break
        guess = collatz(guess)

except:
    print('Enter a valid number!')










