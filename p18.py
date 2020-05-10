# coding=utf-8
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja
# binary search O(q * log(n))

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def bisearch(S, target):
    left, right = 0, len(S)-1

    while right - left > 0:
        mid = left + (right - left) // 2  # to avoid overflowing by (right + left) > right
        if S[mid] < target:
            left = mid + 1
        else:
            right = mid
    return S[left] == target


count = 0
for t in T:
    count += bisearch(S, t)
print(count)

if __name__ == '__main__':
    print(count)



