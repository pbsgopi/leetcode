class Solution:
    def __init__(self):
        self.par = []
        self.rank = []

    def find_parent(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find_parent(self.par[x])
        return self.par[x]

    def union(self, x, y):
        par_x = self.find_parent(x)
        par_y = self.find_parent(y)

        if par_x == par_y:
            return False

        if self.rank[par_x] < self.rank[par_y]:
            par_x, par_y = par_y, par_x

        self.rank[par_x] += self.rank[par_y]
        self.par[par_y] = par_x
        return True

    def removeStones(self, stones):
        n = len(stones)
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        X = {}
        Y = {}
        count = 0

        for i, (x, y) in enumerate(stones):
            if x in X:
                count += self.union(i, X[x])
            else:
                X[x] = i

            if y in Y:
                count += self.union(i, Y[y])
            else:
                Y[y] = i

        return count