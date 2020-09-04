n = int(input())
k = list(map(int, input().split()))
cnt = s = 0
if k[0] % 2 == 0:
    s = sum(k)
while s % 2 == 0:
    for i in range(n):
        if k[i] % 2 != 0:
            break
        cnt += 1
        s /= 2
print(cnt)
