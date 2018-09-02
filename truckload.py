import sys
import itertools

def sortTrucks(a, possible_combination, total_lst):
   #print(a)
   indices = total_lst - possible_combination
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
       del a[-indices:]
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
    lst = sortTrucks(lst, possible_combinations, len(lst))
    result = lst[-1:]
    return result[0][t]

if __name__ == '__main__':
    boxes = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [3],
        [1, 2, 3, 4, 5],
        [2, 5],
        [2, 3, 5],
        [2, 2, 8],
        [2, 3, 5],
        [4, 5, 6, 7, 8],
        [2, 5, 6, 7, 8, 14],
        [2, 5, 5, 8, 10, 12, 18, 19, 20],
        [2, 5, 5, 8, 10, 12, 18, 19, 21]

    ]

    trucks = [
        3,
        1,
        3,
        10,
        10,
        2,
        2,
        2,
        3,
        2,
        3,
        3,
        3
    ]

    expected_result = [
        1,
        0,
        0,
        3,
        5,
        3,
        0,
        4,
        3,
        0,
        0,
        0,
        1
    ]

    for i in range(len(trucks)):
        result = solution(boxes[i], trucks[i])
        if expected_result[i] != result:
            print("Box of list ", boxes[i], " With trucks ", trucks[i], " Failed Output : ", result, " expected output ", expected_result[i])
            #break
        else:
            print("Box of list ", boxes[i], " With trucks ", trucks[i], " Passed Output : ", result)
