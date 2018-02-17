
TESTCASES_FILE = "tinyUF.txt"


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

        if self._size[large] > self._maxsites:
            self._maxsites = self._size[large]

        if p in self._isolated:
            self._isolated.remove(p)

        if q in self._isolated:
            self._isolated.remove(q)

        self._count -= 1

    def isnonisolated(self):
        """
        Checks if there are no isolated components
        :return: True if there are no isolated components, else False
        """

        return len(self._isolated) == 0

    def connected(self, p, q):
        """
        Returns true if the two sites are in the same component.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return:  true if the two sites p and q are in the same component;
                  false otherwise
        """
        return self.find(p) == self.find(q)

    @property
    def maxsites(self):
        return self._maxsites

    @property
    def count(self):
        return self._count

    def find(self, p):
        """
        Returns the component identifier for the component containing site p.

        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        parent = self._parent[p]

        if parent == p:
            return parent

        # path compression
        self._parent[p] = self.find(parent)

        return self._parent[p]


n = None
links = []

with open(TESTCASES_FILE, 'r') as f:
    contents = f.readlines()
    n = int(contents[0].strip())
    links = [tuple(map(int, link.split())) for link in contents[1:]]

giant, connected, non_isolated = None, None, None

uf = MyUnionFind(n)
round_num = 0

for u, v in links:
    round_num += 1

    uf.union(u, v)

    if not non_isolated and uf.isnonisolated():
        non_isolated = round_num
    if not giant and uf.maxsites >= n * 0.5:
        giant = round_num
    if not connected and uf.count == 1:
        connected = round_num


print(giant, connected, non_isolated)
