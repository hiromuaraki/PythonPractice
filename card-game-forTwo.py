
#自分のロジック-------------------------------------------
n = int(input())
c = list(map(int, input().split()))
#無駄な変数
alice = bob = 0
#1.リスト変換から並べ換えは一括でまとめる
card = sorted(c, reverse=True)
#2.無駄なループ
for i in range(n):
    if i % 2 == 0:alice += card[i]
    else:bob += card[i]
#3.最後の結果だけsumればいい
print(alice - bob)

#他の人のロジック------------------------------------------
n = int(input())
#リストへ変換、降順へ並べ換える[20, 18, 2, 18] →[20, 18, 18, 2]
a = sorted(list(map(int, input().split())), reverse=True)
#先頭から２つずつ取得[20, 18] - [18, 2]
print(sum(a[::2]) - sum(a[1::2]))