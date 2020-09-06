n = int(input())
c = list(map(int, input().split()))
alice = bob = 0
card = sorted(c, reverse=True)
#n枚のカード枚数分繰り返す
for i in range(n):
    if i % 2 == 0:alice += card[i]
    else:bob += card[i]
#alice bobの勝敗を求める
print(alice - bob)