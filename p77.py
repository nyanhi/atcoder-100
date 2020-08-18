# https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a

n, m = map(int, input().split())
MOD = 10**5

S = []
for i in range(n-1):
    s = int(input())
    S.append(s)


# 宿場町1を0とした場合に、M[i]は宿場町i+1の位置を表す
M = [0]
for i in range(n-1):
    M.append(M[i] + S[i])


move = 0
start = 0
debug = []
for j in range(m):
    a = int(input())
    move += abs(M[start+a] - M[start]) % MOD
    start = start + a

print(move % MOD)
