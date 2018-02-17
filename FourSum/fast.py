from __future__ import print_function
import sys
 
N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))
vals.sort()
if len(vals) <= 3:
    print(False)
else:
    for i in range(0, N - 3):
        for j in range(i + 1, N - 2):
            k = j + 1
            l = N - 1
            while k < l:
                if vals[i] + vals[j] + vals[k] + vals[l] == 0:
                    print(i, j, k, l, file=sys.stderr)
                    k = k + 1
                    l = l - 1
                    print(True)
                    sys.exit()
                elif vals[i] + vals[j] + vals[k] + vals[l] < 0:
                    k = k + 1
                else:
                    l = l - 1
                    print(False)
                    sys.exit()
