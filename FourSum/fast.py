# Prints True if found False if unfound

### Problem needs to fix: it didn't pass A_50weed1.txt. Outcome should be: True but it turned out False


from __future__ import print_function
import sys
import time


def four_sum(vals):
    vals.sort()
    result = False

    if len(vals) >= 3:
        # fix first elem
        for i in range(N - 3):
            # fix second elem
            for j in range(i + 1, N - 2):
                # third elem
                k = j + 1
                # fourth elem
                l = N - 1
                while k < l:
                    val_sum = vals[i] + vals[j] + vals[k] + vals[l]
                    if val_sum == 0: # Provided by teacher, don't change
                        result = True
                        print(i, j, k, l, file=sys.stderr) # Provided by teacher, don't change
                        return result
                        """
                        print(True) # Provided by teacher, don't change
                        sys.exit() # Provided by teacher, don't change
                        """
                    elif val_sum < 0:
                        k = k + 1
                    else:
                        l = l - 1
    return result


def measure_exec_time(func, *args):
    start = time.time()
    print(func(*args))
    return time.time() - start


if __name__ == "__main__":
    N = int(sys.stdin.readline()) # Provided by teacher, don't change

    """
    # was not working in my interpreter
    vals = list(map(int, sys.stdin.readlines())) # Provided by teacher, don't change
    """

    vals = []
    for x in range(N):
        vals.append(int(input()))

    print(measure_exec_time(four_sum, vals))
