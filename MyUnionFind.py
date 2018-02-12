# EXPECTED OUTCOME AFTER TESTING WITH tinyUF.txt SHOULD BE 10 16 4 16. Mine is 10 -1 4 -1. Need to fix

from algs4.stdlib import stdio
from algs4.stdlib import stdrandom
from algs4.stdlib import stdstats


class MyUnionFind:
    """
        Initializes an empty union-find data structure with n sites,
        0 through n-1. Each site is initially in its own component.
        :param n: the number of sites
        """

    def __init__(self, n):  # MODIFY
        """
        Initializes an empty union-find data structure with n sites,
        0 through n-1. Each site is initially in its own component.
        :param n: the number of sites
        """
        self._count = n
        self._parent = list(range(n))
        self._size = [1] * n
        self._isolated = set()  # DEFINE ISOLATED
        self._maxsites = 1  # DEFINE GIANT
        for i in range(n):  # UPDATE
            self._isolated.add(i)
            self._parent[i] = i
            self._size[i] = 1

    def _validate(self, p):
        # validate that p is a valid index
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError('index {} is not between 0 and {}'.format(p, n))

    def union(self, p, q):  # MODIFY
        """
        Merges the component containing site p with the
        component containing site q.
        :param p: the integer representing one site
        :param q: the integer representing the other site
         """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # make root of smaller rank point to root of larger rank
        if self._size[root_p] < self._size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p

        self._parent[small] = large
        self._size[large] += self._size[small]

        # UPDATE MAX NUMBER OF SITES --- MODIFIED
        if self._maxsites < self._size[root_q]:
            self._maxsites = self._size[root_q]
        if self._maxsites < self._size[root_p]:
            self._maxsites = self._size[root_p]

        if p in self._isolated:
            self._isolated.remove(p)

        if q in self._isolated:
            self._isolated.remove(q)

        self._count -= 1

    def isnonisolated(self):
        """
        If there is no isolated component
        :return: the nonisolated component
        """

        if len(self._isolated) == 0:
            return True
        else:
            return False

    def maxsites(self):  # ADD NEW
        return self._maxsites

    def find(self, p):
        """
        Returns the component identifier for the component containing site p.

        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def connected(self, p, q):
        """
        Returns true if the two sites are in the same component.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        return self.find(p) == self.find(q)

    def count(self):
        return self._count


# GiantBook

t = 1
n = stdio.readInt()
uf = MyUnionFind(n)
connectList = list()
nonisolatedList = list()
giantList = list()

for j in range(t):
    nonisolated = -1
    giant = -1
    connected = - 1
    giantList.append(giant)
    nonisolatedList.append(nonisolated)
    connectList.append(connected)

    for i in range(n):
        p = stdio.readInt()
        q = stdio.readInt()
                # Check if nonisolated exists
        if uf.isnonisolated() and nonisolated == -1:
            nonisolated = i
                # Check if giant component exists
        if uf.maxsites() >= (n * 0.5) and giant == -1:
            giant = i
                # Connect
        if uf.count() == 1:
            connected = i

                # Union p, q
        if uf.connected(p, q):
            continue
        uf.union(p, q)

    giantList[j] = giant
    nonisolatedList[j] = nonisolated
    connectList[j] = connected

    print(n, nonisolatedList[j], giantList[j], connectList[j], end=" ")
