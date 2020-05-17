# coding=utf-8
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

# DFS - O(W*H) as dfs will run on at max once on each element
import sys
sys.setrecursionlimit(200000)
readline = sys.stdin.buffer.readline


def dfs(C, h, w):
    # 一度訪ねた陸地は'0'(海)に置き換える
    C[h][w] = '0'
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= h+i < len(C) and 0 <= w+j < len(C[0]) and C[h+i][w+j] == '1':
                dfs(C, h+i, w+j)


W, H = 1, 1
while W != 0 or H != 0:
    W, H = map(int, input().split())
    C = []
    for h in range(H):
        c = list(input().split())
        #c = readline().split()
        C.append(c)

    count = 0
    for h in range(H):
        for w in range(W):
            if C[h][w] == '1':
                dfs(C, h, w)
                count += 1
    if W != 0 or H != 0:
        print(count)

