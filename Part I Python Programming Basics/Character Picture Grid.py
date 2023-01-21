grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for y in range(5): #9
    #print(len(grid[y]))
    for x in range(9):
        print(grid[x][y], end = ' ')

    print()


for y in range(5, -1, -1): #9
    #print(len(grid[y]))
    for x in range(8, -1, -1):
        print(grid[x][y], end = ' ')

    print()
