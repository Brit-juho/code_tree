n = int(input())

for i in range(1, n+1):
    if i % 2 != 0:
        print(''.join(str(j) for j in range(1, n+1)))
    else:
        print(''.join(str(j) for j in range(n, 0, -1)))