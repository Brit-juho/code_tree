grid1 = [[int(x) for x in input().split()] for j in range(3)]

_ = input()

grid2 = [[int(x) for x in input().split()] for j in range(3)]

for a in range(3):
    for b in range(3):
        grid1[a][b] = grid1[a][b] * grid2[a][b]

        if b == 2:
            print(grid1[a][b])
        else:
            print(grid1[a][b], end=' ')