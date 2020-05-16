# coding=utf-8

from math import log

P = float(input())


def func(x):
    return x + P * 2 ** (-x / 1.5)


# 導関数が単調なので、二分探索で零点(i.e. の臨界点)を見つける
def df(x):
    return 1 - P * log(2) / 1.5 * 2 ** (-x / 1.5)


def bisearch(x):
    left, right = 0.0, P
    while right - left > 1e-9:
        mid = left + (right - left) / 2.0
        if df(mid) < x:
            left = mid
        else:
            right = mid
    return left


crit_p = bisearch(0)

if 0 < crit_p <= P:
    print(func(crit_p))
else:
    print(func(0))

if __name__ == '__main__':
    print(func(crit_p))
