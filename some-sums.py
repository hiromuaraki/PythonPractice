#入力値を受け取り分割し、アンパック代入
n, a, b = [int(_) for _ in input().split()]
ans = 0
#1-n + 1回数分繰り返す
for i in range(1, n + 1):
    if a <= sum(map(int, list(str(i)))) <= b:
        ans += i
print(ans)