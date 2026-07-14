n, m = map(int, input().split())

grid1 = [[int(x) for x in input().split()] for _ in range(n)]
grid2 = [[int(x) for x in input().split()] for _ in range(n)]
grid_sul = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid2[i][j] != grid1[i][j] :
            grid_sul[i][j] = 1
    print(*grid_sul[i])

