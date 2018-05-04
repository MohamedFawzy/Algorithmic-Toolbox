import random
from max_pairwise_product import max_pairwise_product_naive
from max_pairwise_product import max_pairwise_product


def stress_testing(N, M):
    print "Hello"
    while True:
        n = random.randint(2, N)
        a = a[1:n]
        for i in range(0, n):
            a[i] = random.randint(0, M)
        print(a[i:n])
        result1 = max_pairwise_product_naive(N , a)
        result2 = max_pairwise_product(N , a)
        if result1 == result2:
            print "OK"
        else:
            print ("Wrong answer: ", result1, result2)
            return


if __name__ == '__main__':
    N = raw_input('enter N : ')
    M = raw_input('enter M')
    print(stress_testing(N, M))


