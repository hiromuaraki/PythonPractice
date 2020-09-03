cnt = 0
while cnt == 0:
    x, y = map(int, input().split())
    for i in range(x):
        for j in range(y):
            if j < y:
                print("#", end="")
            else:
                break
        print()
    if x == 0 or y == 0:
        cnt = -1
        break
    print()
