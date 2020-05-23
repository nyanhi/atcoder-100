# coding=utf-8
# https://atcoder.jp/contests/abc138/tasks/abc138_d

# 木を探索する途中にO(N)、値を加算していく
import sys
input = sys.stdin.buffer.readline  # これを使わないとTLEしてしまう
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
AB = [[int(x) for x in input().split()] for _ in range(N-1)]
PX = [[int(x) for x in input().split()] for _ in range(Q)]

# 木構造をリストで表現する
graph = [[] for _ in range(N+1)]

for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)

# 各操作で与えられる値を、各頂点ごとに集計しておく
P = [0] * (N+1)
for p, x in PX:
    P[p] += x


def dfs(v, parent, point):
    # 現在いる頂点vの親までの値をpointとする
    P[v] += point
    for x in graph[v]:
        if x == parent:
            continue
        dfs(x, v, P[v])


dfs(1, 0, 0)

res = ' '.join(map(str, P[1:]))
print(res)


