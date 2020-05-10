# https://atcoder.jp/contests/sumitrust2019/custom_test
# brute-force, computational complexity O(k^2) because 2 slices are nested

N = int(input())
S = input()

codes = set()

S1 = S[:N - 2]
for i in set(S1):
    idx1 = S1.index(i)
    S2 = S1[idx1 + 1:] + S[N - 2]
    for j in set(S2):
        idx2 = S2.index(j)
        S3 = S2[idx2 + 1:] + S[N - 1]
        for k in set(S3):
            pin = i + j + k
            codes.add(pin)

print(len(codes))
