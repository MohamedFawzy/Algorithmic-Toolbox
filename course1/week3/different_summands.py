# Uses python2
import sys


def optimal_summands(n):
    summands = []
    k = n  # marked as lower part
    i = 1
    # write your code here
    while (i < n + 1):
        k = k - i
        if k == 0:
            summands.append(i)
            break
        if k <= i:
            summands.append(k + i)
            break
        else:
            summands.append(i)
            i += 1

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print str(x) + " ",
