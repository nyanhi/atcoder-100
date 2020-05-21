# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e

# S -> 1 -> 2 -> ...の順に周る最短距離をBFSを繰り返して求める
# 計算量はO(H*W*N)
import sys
from collections import deque
sys.setrecursionlimit(10**7)

H, W, N = map(int, input().split())
factories = ['S', '1', '2', '3', '4', '5', '6', '7', '8', '9']
goals = {}

G = []
for i in range(H):
    tmp = list(input())
    G.append(tmp)
    for c in factories:
        if c in tmp:
            j = tmp.index(c)
            if c == 'S':
                c = '0'
            goals[int(c)] = (i, j)

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


def BFS(sy, sx, gy, gx):
    que = deque()
    que.append((sy, sx))

    d = [[-1] * W for _ in range(H)]
    d[sy][sx] = 0

    while que:
        cy, cx = que.popleft()
        for dire in directions:
            ny, nx = cy + dire[0], cx + dire[1]
            if 0 <= ny < H and 0 <= nx < W:
                if G[ny][nx] != 'X' and d[ny][nx] < 0:  # 範囲内かつ、訪ねていない
                    d[ny][nx] = d[cy][cx] + 1
                    que.append((ny, nx))
        # 終了条件 d[gy][gx]>0だったらreturn
        if d[gy][gx] > 0:
            return d[gy][gx]


res = 0
for n in range(N):
    sy, sx = goals[n]
    gy, gx = goals[n+1]
    res += BFS(sy, sx, gy, gx)

print(res)
