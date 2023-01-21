import random

n_exp = 10_000
n_streak = 0
for experiment in range(n_exp):
    draw = ''.join(random.choices('HT', k=100))
    if 'H'*6 in draw or 'T'*6 in draw:
        n_streak += 1

res = n_streak / n_exp * 100
print(res)
