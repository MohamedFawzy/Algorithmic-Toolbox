import random
from max_pairwise_product_naive import max_pairwise_product_naive
from max_pairwise_product import max_pairwise_product




N = 10
M = 100000



def stressTesting(N, M):
    print "Hello"
    while True:
        n =  random.randint(2, N)
        a = a[1:n]
        for i in range(1, n):
            a[i] = random.randint(0, M)
        print(a[i:n])
        result1 = max_pairwise_product_naive(a)
        result2 = max_pairwise_product(a)
        if result1 == result2:
            print "OK"
        else:
            print ("Wrong answer: ", result1, result2)
            return

stressTesting(N, M)
