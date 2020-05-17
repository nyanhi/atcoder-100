# coding=utf-8
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_B&lang=ja

# calculate m ** n mod (10 ** 9 + 7)
# As 3 ** 7 = 3 ** (2**0 + 2**1 + 2**2), in general write m in binary such as m = 0111b
# O(log(n))


def modpow(m, n, mod):
    # ref. built-in function pow(m, n, mod)
    res = 1
    while n > 0:
        if n & 1:
            res = res * m % mod
        m = m * m % mod
        n >>= 1
    return res


m, n = map(int, input().split())
mod = 10 ** 9 + 7

print(modpow(m, n, mod))



