count = 0
count2 = 0
for i in range(10):
    p = int(input())
    if p % 3 == 0:
        count += 1
    if p % 5 == 0:
        count2 += 1
print(count, count2)