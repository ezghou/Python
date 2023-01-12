m = 10
n = 10

a = [[0 for x in range(n)] for x in range(m)]

for i in range(len(a)) :
    for j in range(len(a[i])) :
        print(a[i][j], end="  ")
    print()
