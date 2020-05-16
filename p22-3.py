# coding=utf-8
from scipy.optimize import fmin

# scipy.optimize.fimを使って最小値を求める

P = float(input())


def func(x):
    # fminによって探索する範囲を x >= 0 に制限するため
    if x < 0:
        return P * 10
    return x + P * 2 ** (-x/1.5)


xopt = fmin(func, 0, xtol=1e-10, disp=False)

print(func(xopt[0]))

