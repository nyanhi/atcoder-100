# https://atcoder.jp/contests/abc034/tasks/abc034_c

# (1, 1)から(W, H)にたどり着くまで、横方向にW-1回、縦方向にH-1回移動する。
# それらの移動の組み合わせが経路の個数に一致する. 二項係数Combination(W-1 + H-1, W-1)を計算する

# 1<= W <= 10 ** 5に対して(W+H-2)!は大きすぎて計算できないので、適宜mod (10**9 + 7)を取りながら計算する
# 10**9 + 7は素数なので、フェルマーの小定理を利用して、
# (W-1)!で割る代わりに、逆元をかける

W, H = map(int, input().split())
mod = 10**9 + 7

fact = [1] * (W+H+1)

for n in range(1, W+H+1):
    fact[n] = (fact[n-1] * n) % mod

# fact[W-1], fact[H-1]の mod 10**9+7 での逆元を求める
# fact[W-1] ** (10**9+5) が逆元となる (フェルマーの小定理)
fact_inv_W = pow(fact[W-1], mod-2, mod)
fact_inv_H = pow(fact[H-1], mod-2, mod)

# 2項係数を逆元を使って計算する
res = ((fact[W+H-2] * fact_inv_W) % mod) * fact_inv_H % mod
print(res)

