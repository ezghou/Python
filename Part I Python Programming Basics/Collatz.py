

def collatz(number):
    if number % 2 == 0:
        ans = number // 2
        print(ans)
        return ans

    else:
        answer = 3 * number + 1
        print(answer)
        return answer

print('Enter a number: ', end = '')
guess = int(input())

while True:
    if guess == 1:
        break
    guess = collatz(guess)

