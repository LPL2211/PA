# A simple Python 3 program
# to find four elements whose
# sum is equal to zero
 
# Prints True if found False if unfound

### Problem needs to fix: it didn't pass A_50weed1.txt. Outcome should be: True but it turned out False
 
 
from __future__ import print_function
import sys
 
N = int(sys.stdin.readline()) # Provided by teacher, don't change
vals = list(map(int, sys.stdin.readlines())) # Provided by teacher, don't change
if len(vals) <= 3:
    print(False)
else:
    for i in range(0, N - 3):
        for j in range(i + 1, N - 2):
            for k in range(j + 1, N - 1):
                for l in range(k + 1, N):
                    if vals[i]+vals[j]+vals[k]+vals[l] == 0: # Provided by teacher, don't change
                        print(i, j, k, l, file=sys.stderr) # Provided by teacher, don't change
                        print(True) # Provided by teacher, don't change
                        sys.exit() # Provided by teacher, don't change
                    elif vals[i] + vals[j] + vals[k] + vals[l] < 0:
                        k = k + 1
                    else:
                        l = l - 1
                        print(False)
                        sys.exit()
