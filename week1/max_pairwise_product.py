# Uses python2
import random


# find max pairwise product
def max_pairwise_product_naive(n, a):
    result = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if a[i] * a[j] > result:
                result = a[i] * a[j]

    return result


# optimized version of max pairwise product
# instated of iterate through two indices which is O(n^2) get first one then next one alone

def max_pairwise_product(n, a):
    max_index1 = -1

    for i in range(n):
        if max_index1 == -1 or a[i] > a[max_index1]:
            max_index1 = i

    max_index2 = -1

    for j in range(n):
        if a[j] != a[max_index1] and (max_index2 == -1 or a[j] > a[max_index2]):
            max_index2 = j

    return a[max_index1] * a[max_index2]


if __name__ == '__main__':
    ##### stress test as validation model for our algorithm ######
    while (True):
        n = random.randrange(2, 10)
        print "generated random numbers ", n
        a = []
        for i in range(n):
            a.append(i)

        print "generated dictionary ", a
        result1 = max_pairwise_product_naive(n, a)
        result2 = max_pairwise_product(n, a)
        if result1 != result2:
            print "Wrong Answer Result ", result1, "Result2 ", result2
            break
        else:
            print  "OK"
    #### end stress testing #####

    n = int(input())
    a = [int(x) for x in raw_input().split()]
    assert (len(a) == n)
    print(max_pairwise_product(n, a))
