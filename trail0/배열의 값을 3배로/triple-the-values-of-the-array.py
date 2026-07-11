grid = []

for i in range(3):
    n = list(map(int, input().split()))
    grid.append(n)

for i in range(3):
    for j in range(3):
        grid[i][j] *= 3

for i in range(3):
    for j in range(3):
        print(grid[i][j], end = " ")
    print()
