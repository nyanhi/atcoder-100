# https://atcoder.jp/contests/abc145/tasks/abc145_d
# X = n + 2m, Y = 2n + m (n, m >= 0) の整数解がひとつ見つかれば、 2項係数combination(n+m, n)を計算すればよい

import sys

X, Y = map(int, input().split())
mod = 10 ** 9 + 7

# 整数解がない場合
if (2 * X - Y) % 3 != 0 or (2 * Y - X) % 3 != 0:
    print(0)
    sys.exit()

m = (2 * X - Y) // 3
n = (2 * Y - X) // 3

# 整数解が負の場合
if m < 0 or n < 0:
    print(0)
    sys.exit()

u = m + n
fact = [1] * (u+1)

for i in range(1, u+1):
    fact[i] = (fact[i-1] * i) % mod

fact_inv1 = pow(fact[n], mod-2, mod)
fact_inv2 = pow(fact[m], mod-2, mod)

res = (((fact[u] * fact_inv1) % mod) * fact_inv2) % mod

print(res)
