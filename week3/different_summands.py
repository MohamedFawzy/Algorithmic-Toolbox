# Uses python2
import sys


def optimal_summands(n):
    summands = []
    k = n  # marked as lower part
    l = 1  # marked as upper part
    # write your code here
    if n == 1 or n == 2:
        summands.append(n)
    else:
        for i in range(k):
            if k <= 2 * l:
                summands.append(k)
                break
            else:
                summands.append(l)
                k = k - l
                l = l + 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print str(x) + " ",
