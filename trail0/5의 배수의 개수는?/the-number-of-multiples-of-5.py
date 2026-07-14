print(
    sum(
         int(x) % 5 == 0 for _ in range(4) for x in input().split()
    )
)