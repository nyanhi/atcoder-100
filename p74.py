# https://atcoder.jp/contests/abc021/tasks/abc021_d

# 1 <= a_1 <= a_2 <= ... <= a_k <= n なる {a_i}の選び方は、二項係数Combination(n+k-1, k)通りある
# 重複組み合わせ

n = int(input())
k = int(input())
mod = 10 ** 9 + 7

fact = [1] * (n+k+1)

for i in range(1, n+k+1):
    fact[i] = (fact[i-1] * i) % mod

fact_inv1 = pow(fact[n-1], mod-2, mod)
fact_inv2 = pow(fact[k], mod-2, mod)

res = (((fact[n+k-1] * fact_inv1) % mod) * fact_inv2) % mod

print(res)

