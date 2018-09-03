# Uses python2
import sys


def optimal_summands(n):
    summands = []
    k = n  # marked as lower part
    # write your code here
    for i in range(1, n + 1):
        k = k - i
        if k == 0:
            summands.append(i)
            break
        if k <= i:
            summands.append(k + i)
            break
        else:
            summands.append(i)

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print str(x) + " ",
