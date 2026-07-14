
grid = [[int(x) for x in input().split()] for _ in range(4)]

for row in grid:
    grid_sum = sum(row)
    print(grid_sum)