n = input()
a = ''
for i in range(len(n)):
    if i == 1 or i == len(n)-2:
        a += 'a'
    else: a += n[i:i+1:]
print(a)