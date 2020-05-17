# coding=utf-8
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja

# memoize

memo = {}


def fib(n):
    """
    :param n: non-negative integer
    :return: n-th fibonacci number
    """
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        pass

    res = fib(n-1) + fib(n-2)
    memo[n] = res

    return res


n = int(input())
print(fib(n))



