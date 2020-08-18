#!/usr/bin/env python3
# https://atcoder.jp/contests/nikkei2019-final/tasks/nikkei2019_final_a

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

S = [0]

for i in range(N):
    S.append(S[i]+A[i])

for k in range(1, N+1):
    max_sum = 0
    for i in range(N-k+1):
        max_sum = max(max_sum, S[k+i] - S[i])
    print(max_sum)
