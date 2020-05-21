# https://atcoder.jp/contests/abc007/tasks/abc007_3
# 重みなしグラフの最短経路をBFSを使ってもとめる。計算量は状態数 R*Cと4方向の遷移4によって O(4*R*C) = O(R*C)
import sys
from collections import deque
sys.setrecursionlimit(10**6)


R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

G = [list(input()) for _ in range(R)]

# index starts from 0
sy, sx = sy-1, sx-1
gy, gx = gy-1, gx-1

# sy, sxからの最短距離を保持する
d = [[-1] * C for _ in range(R)]

que = deque()
que.append((sy, sx))
d[sy][sx] = 0

# 4方向の遷移
directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

while que:
    py, px = que.popleft()
    for dire in directions:
        ny, nx = py+dire[0], px+dire[1]
        if 0 <= ny < R and 0 <= nx < C:  # 周囲は壁で囲まれているので、実は必要ない条件
            if G[ny][nx] != '#' and d[ny][nx] < 0:  # 壁ではなく、訪問したことがない
                que.append((ny, nx))
                d[ny][nx] = d[py][px] + 1

print(d[gy][gx])


if __name__ == '__main__':
    print(d)
