#Uses python2

import sys
def comparator(a,b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return cmp(int(ba), int(ab))
def largest_number(a):
    #write your code here
    a = sorted(a, cmp=comparator)
    res = ""
    for x in a:
        res += x

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
