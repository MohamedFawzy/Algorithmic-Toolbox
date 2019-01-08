# Uses python2
import sys
import math


def optimal_summands(n):
    sol = int((math.sqrt(1 + 8 * n) - 1) / 2)
    print sol
    for i in range(1, sol):
        print str(i) + " ",
    diff = n - ((sol * sol + sol) / 2)
    print sol + diff


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    optimal_summands(n)
