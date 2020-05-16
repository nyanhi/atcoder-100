# coding=utf-8
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A&lang=ja

# DFSでbit全探索する。Aの要素が全て自然数であることを利用して、枝刈りする

n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))


def dfs(idx, sum_, target):
    if sum_ == target:
        return True

    # Aの要素は全て正の数なので、targetを超えたら枝刈り
    if sum_ > target or idx == n:
        return False

    # idx項以降のAの要素を全て足してもtargetより小さい場合は枝刈り
    if sum_ + sum(A[idx:]) < target:
        return False

    return dfs(idx+1, sum_, target) or dfs(idx+1, sum_+A[idx], target)


for target in M:
    if dfs(0, 0, target):
        print('yes')
    else:
        print('no')

