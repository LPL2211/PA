## Still doesn't work with random number (see below) --> Fixed
## Get error when finding mean and sdtdev using stdstats. TypeError: 'int' object is not iterable --> Fixed
## What is T in this source code? It's the variable "round_num"

from __future__ import division
from algs4.stdlib import stdio, stdrandom, stdstats


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


if __name__ == '__main__':

    n = 10

    # To calculate the mean, std_deviation, etc with random numbers
    # we need to run the experiment "num_episodes" times.
    num_episodes = 100
    num_links_default = 2*n

    giant, connected, non_isolated = None, None, None

    uf = MyUnionFind(n)

    # This is the 'T' in your book
    round_num = 0

    choice = input(""" Please enter
        1 to read from the file.
        2 for random numbers
        3 to enter links on your own \n\t""")

    giant_timings = []
    connected_timings = []
    non_isolated_timings = []

    if choice == "1":
        file_path = input("Enter file path")
        links = []
        with open(file_path, 'r') as f:
            contents = f.readlines()
            n = int(contents[0].strip())
            links = [tuple(map(int, link.split())) for link in contents[1:]]
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

    if choice == "2":
        for i in range(num_episodes):
            uf = MyUnionFind(n)
            giant, connected, non_isolated = None, None, None
            for j in range(num_links_default):
                p = stdrandom.uniformInt(0, n)
                q = stdrandom.uniformInt(0, n)

                round_num += 1

                uf.union(p, q)

                if not non_isolated and uf.isnonisolated():
                    non_isolated = round_num
                    non_isolated_timings.append(non_isolated)
                if not giant and uf.maxsites >= n * 0.5:
                    giant = round_num
                    giant_timings.append(giant)
                if not connected and uf.count == 1:
                    connected = round_num
                    connected_timings.append(connected)

            print(n, non_isolated, giant, connected) # OUTCOME OF NON-ISOLATED AND CONNECTED ARE ALWAYS NONE. PLEASE HELP TO FIX

        if len(giant_timings):
            giant_mean = stdstats.mean(giant_timings)
            giant_median = stdstats.median(giant_timings)
            giant_stddev = stdstats.stddev(giant_timings)
            stdio.eprint(giant_mean, giant_median, giant_stddev)

        if len(connected_timings):
            connected_mean = stdstats.mean(connected_timings)
            connected_median = stdstats.median(connected_timings)
            connected_stddev = stdstats.stddev(connected_timings)
            stdio.eprint(connected_mean, connected_median, connected_stddev)

        if len(non_isolated_timings):
            non_isolated_mean = stdstats.mean(non_isolated_timings)
            non_isolated_median = stdstats.median(non_isolated_timings)
            non_isolated_stddev = stdstats.stddev(non_isolated_timings)
            stdio.eprint(non_isolated_mean, non_isolated_median, non_isolated_stddev)

    if choice == "3":
        num_links = int(input("Enter the number of links you want to enter"))

        for x in range(num_links):
            p = stdio.readInt()
            q = stdio.readInt()

            round_num += 1

            uf.union(p, q)

            if not non_isolated and uf.isnonisolated():
                non_isolated = round_num
            if not giant and uf.maxsites >= n * 0.5:
                giant = round_num
            if not connected and uf.count == 1:
                connected = round_num

        print(giant, connected, non_isolated)
