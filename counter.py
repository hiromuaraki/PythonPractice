# coding: utf-8
# Your code here!
import collections

n = int(input())
# 行数分繰り返し入力値をリストへ変換し、格納する
d = list(map(int, [input() for i in range(n)]))
# Counter([key : 値]) データをグルーピングしている
k = collections.Counter(d)
print(len(k))

  