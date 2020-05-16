# coding=utf-8

from math import log, log2

P = float(input())


def func(y):
    return y + P * 2 ** (- y / 1.5)


# func(y)の解析的な臨界点
x = 1.5 * log2(P / 1.5 * log(2))

# funcの微分は単調増加 (i.e. func is convex)なので、臨界点が 0 < x <= Pにあれば最小値はfunc(x)
if 0 < x <= P:
    print(func(x))
else:
    print(P)

