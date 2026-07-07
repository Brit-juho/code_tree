A = input().split()
B = []
for i in range(9, -1, -1):
    B.append(A[i])
for ch in B:
    print(ch,end=(''))