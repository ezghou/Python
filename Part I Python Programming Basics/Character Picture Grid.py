grid = [['.00','.01', '.02', '.03', '.04', '.05'],
        ['.10', 'O11', 'O12', '.13', '.14', '.15'],
        ['O20', 'O21', 'O22', 'O23', '.24', '.25'],
        ['O30', 'O31', 'O32', 'O33', 'O34', '.35'],
        ['.40', 'O41', 'O42', 'O43', 'O44', 'O45'],
        ['O50', 'O51', 'O52', 'O53', 'O54', '.55'],
        ['O60', 'O61', 'O62', 'O63', '.64', '.65'],
        ['.70', 'O71', 'O72', '.73', '.74', '.75'],
        ['.80', '.81', '.82', '.83', '.84', '.85']]


for y in range(6): #9
    #print(len(grid[y]))
    for x in range(9):
        print(grid[x][y], end = ' ')

    print()