# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 1))
        self.size = [1] * (n + 1)

    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            x, y = y, x
            sx, sy = sy, sx
        self.root[y] = x
        self.size[x] += sy


n, q = map(int, input().split())
uni = UnionFind(n)

for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        uni.merge(x, y)
    else:
        print(int(uni[x] == uni[y]))

