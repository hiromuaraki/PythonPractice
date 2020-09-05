#自分のロジック
n = int(input())
k = list(map(int, input().split()))
cnt = r =  0
if k[0] % 2 == 0:
    r = sum(k)
    while r % 2 == 0:
        r /= 2
        cnt += 1
print(cnt)

#他の人のロジック
n = input()
a = list(map(int, input().split()))
#無限大の数を取得
ans = float('inf')
#[入力値の要素]数文繰り返す
for i in a:
    #10進数→2進数へ変換　例:8→0b1000→6
    #rfind('1')が最初に登場するインデックス番号
  ans = min(ans, len(bin(i)) - bin(i).rfind('1') - 1)
print(ans)