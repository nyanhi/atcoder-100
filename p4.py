# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
# brute-force, computational complexity O(N*M^2)

N, M = map(int, input().split())
A = []

for i in range(N):
    lst = list(map(int, input().split()))
    A.append(lst)

max_score = 0
for i in range(M):
    for j in range(i + 1, M):
        score = 0
        for k in range(N):
            score += max(A[k][i], A[k][j])
        max_score = max(max_score, score)

print(max_score)
