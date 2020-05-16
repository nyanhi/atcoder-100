# coding=utf-8
from itertools import product
# itertools.productを使って、bit全探索を行う

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

cases = product([0, 1], repeat=n)

seen = set()

for case in cases:
    sum_ = 0
    for i in range(n):
        sum_ += case[i] * A[i]
    seen.add(sum_)

for target in M:
    if target in seen:
        print('yes')
    else:
        print('no')

