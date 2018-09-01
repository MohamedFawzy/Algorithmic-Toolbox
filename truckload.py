import sys
import itertools

def sortTrucks(a):

   # get first two lists inside the list
   x=  a[0]
   if len(a) > 1:
    y = a[1]
   # remove first two lists from the list of lists
   if len(a)> 1:
    del a[0:2]
   else:
    del a[0]
   # sort list of lists based on second element inside every list as descending order
   a.sort(key=lambda k: (-k[1]))
   #print(a)
   # delete last two items inside the list
   if len(a) > 1:
       del a[-2:]
   else:
       del a[-1:]
   #print(a)
   # add the items to list again
   a.append(x)
   if len(a)> 1:
    a.append(y)
   #print(a)
   # sort them
   a = sorted(a, key=lambda i: [-i[0]])
   #print(a)
   return a


def solution(w, t):
    sum_weights = sum(w)
    total_w = xrange(0,sum_weights+1)
    list_length = len(w)
    possible_combinations = list_length * t

    comp   = itertools.combinations_with_replacement(total_w, t)

    lst = list()

    for i in list(comp):
        if sum(i) == sum_weights:
            i = i[::-1]
            i = list(i)
            i.append(max(i)-min(i))
            lst.append(i)


    lst = sorted(lst, key=lambda i:[-i[0]])
    # get min value from column three
    lst = sortTrucks(lst)
    return min(min(lst))

if __name__ == '__main__':
    input = sys.stdin.readline()
    # boxes weights
    w = list(map(int, input.split()))
    # number of trucks
    t = int(sys.stdin.readline())
    result = solution(w, t)
    print(result)