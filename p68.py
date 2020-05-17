# coding=utf-8
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A&lang=ja

from math import sqrt

n = int(input())
orig_n = n

factor = []

i = 2
while i <= sqrt(n):
    if n % i == 0:
        factor.append(i)
        n //= i
    else:
        i += 1

if n != 1:
    factor.append(n)

res = f'{orig_n}: ' + ' '.join(map(str, factor))

print(res)

