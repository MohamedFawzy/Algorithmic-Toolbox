# Uses python2
import sys


def get_change(m):
    # write your code here
    a, b, c = 1, 5, 10
    count = 0
    while m > 0:
        if m >= c:
            count += m // c
            m %= c
        elif m >= b:
            count += m // b
            m     %= b
        else:
            count += m // a
            break


    return m


if __name__ == '__main__':
    m = int(raw_input())
    m = 28
    print(get_change(m))
