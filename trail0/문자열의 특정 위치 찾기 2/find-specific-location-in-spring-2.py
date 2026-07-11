le = ["apple", "banana", "grape", "blueberry", "orange"]

a = input()
count = 0
for i in le:
    if i[2] == a or i[3] == a:
        print(i)
        count += 1

print(count)
