n = int(input())
k = list(map(int, input().split()))
cnt = r =  0
if k[0] % 2 == 0:
    r = sum(k)
    while r % 2 == 0:
        r /= 2
        cnt += 1
print(cnt)