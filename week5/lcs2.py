# Uses python2

import sys


def lcs2(a, b):
    print(a, b)
    # write your code here
    # find the length of the strings
    m = len(a)
    n = len(b)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in xrange(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


if __name__ == '__main__':
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    m = int(raw_input())
    b = list(map(int, raw_input().split()))
    print(lcs2(a,b))
