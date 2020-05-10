# coding=utf-8
# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

N = int(input())

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

INF = float('inf')
min_dist = INF

# 入口、出口はA, Bのいずれかに一致する場合が最小
for x in A:
    for y in B:
        sum_dist = 0
        for i in range(N):
                sum_dist += min(abs(x-A[i])+abs(A[i]-B[i])+abs(B[i]-y), abs(x-B[i])+abs(B[i]-A[i])+abs(A[i]-y))
        min_dist = min(min_dist, sum_dist)

print(min_dist)



