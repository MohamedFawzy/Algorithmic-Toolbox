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

def max_pairwise_product(n, a):
    max_index1 = 0

    for i in range(n):
        if a[i] > a[max_index1]:
            max_index1 = i

    if max_index1 == 0:
        max_index2 = 1
    else:
        max_index2 = 0

    for j in range(n):
        if a[j] != a[max_index1] and a[j] > a[max_index2]:
            max_index2 = j

    return a[max_index1] * a[max_index2]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in raw_input().split()]
    assert (len(a) == n)
    #print('naive', max_pairwise_product_naive(n, a))
    #print('fast', max_pairwise_product(n, a))
    print(max_pairwise_product(n,a))
