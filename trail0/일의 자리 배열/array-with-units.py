arr = list(map(int, input().split()))

for i in range(8):
    n = (arr[i] + arr[i+1])
    arr.append(n%10)
print(*arr)
