import sys
import itertools

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
    print(lst)
    # get min value from column three
    return min(lst[3])


if __name__ == '__main__':
    input = sys.stdin.readline()
    # boxes weights
    w = list(map(int, input.split()))
    # number of trucks
    t = int(sys.stdin.readline())
    result = solution(w, t)
    print(result)