# Uses python2

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

def max_pairwise_product(n , a):

    index1 = 1

    for i in range(0, n):
        if a[i] > a[index1]:
            index1 = i

    if index1 == 1:
        index2 = 2
    else:
        index2 = 2

    for j in range(1, n):
        if a[j] != a[index1] and a[j] != a[index2]:
            index2 = j

    return a[index1] * a[index2]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in raw_input().split()]
    assert(len(a) == n)
    print('naive', max_pairwise_product_naive(n, a))
    print('fast', max_pairwise_product(n, a))



