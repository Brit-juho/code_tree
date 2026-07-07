n = int(input())

for i in range(1, n+1):
    c = [f'{i}' for j in range(i)]
    print(*c, sep=' ')