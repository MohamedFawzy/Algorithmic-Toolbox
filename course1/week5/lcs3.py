# Uses python2

import sys


def lcs3(a, b, c):
    m = len(a)
    n = len(b)
    p = len(c)
    L = [[[None for k in xrange(p + 1)] for j in xrange(n + 1)] for i in xrange(m + 1)]
    for i in xrange(m + 1):
        for j in xrange(n + 1):
            for k in xrange(p + 1):
                if (i == 0 or j == 0 or k == 0):
                    L[i][j][k] = 0
                elif (a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]):
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else:
                    L[i][j][k] = max(L[i - 1][j][k], L[i][j - 1][k], L[i][j][k - 1], L[i - 1][j - 1][k],
                                     L[i - 1][j][k - 1], L[i][j - 1][k - 1])
    return L[m][n][p]


if __name__ == '__main__':
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    m = int(raw_input())
    b = list(map(int, raw_input().split()))
    k = int(raw_input())
    c = list(map(int, raw_input().split()))
    print(lcs3(a, b, c))
