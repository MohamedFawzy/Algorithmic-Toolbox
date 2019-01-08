# Uses python2
import random
def naive_calc_fib(n):
    if (n <= 1):
        return n

    return naive_calc_fib(n - 1) + naive_calc_fib(n - 2)

def calc_fib(n):
    if n==0 or n==1:
        return n

    f = range(0,n+1)
    f[0]=0
    f[1]=1

    for i in range(2, n+1):
        f[i] = f[i -1] + f[i - 2]

    return f[n]

if __name__ == '__main__':
    n = int(input())
    efficient = calc_fib(n)
    print efficient

    # stress testing for
    # while(True):
    #     for n in range(0,46):
    #         print("generated random parameter for fibonacci function is ", n)
    #         naive = naive_calc_fib(n)
    #         efficient = calc_fib(n)
    #         print("comparing result for naive algorithm which is ", naive, " to efficient algorithm which is ", efficient)
    #         if naive != efficient:
    #             break

