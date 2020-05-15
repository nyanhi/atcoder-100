# coding=utf-8
# https://atcoder.jp/contests/abc077/tasks/arc084_a

from logging import getLogger, DEBUG, CRITICAL
from bisect import bisect_left, bisect_right

logger = getLogger(__name__)
logger.setLevel(CRITICAL)


def bisearch(S, target):
    """
    S: sorted array in ascendant order
    return how many elements are less than target (< target)
    """
    left, right = 0, len(S)-1
    if target > S[right]:
        return len(S)
    elif target < S[left]:
        return 0

    while right - left > 0:
        mid = left + (right - left) // 2

        if S[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()

count = 0
for b in B:
    upper = bisect_left(A, b)   # returns number of elements which satisfy a < b
    lower = bisect_right(C, b)  # returns number of elements which satisfy b < c
    count += upper * (len(C) - lower)
    logger.warning(f'target, upper, lower: {b}, {A[:upper]}, {C[lower:]}, {upper * (len(C) - lower)}')

print(count)




