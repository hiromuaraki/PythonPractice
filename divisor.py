import sympy
a, b, c = map(int, input().split())
cnt = 0
# 約数を求める
for i in range(a, b + 1):
    if c % i == 0: cnt += 1
print(cnt)