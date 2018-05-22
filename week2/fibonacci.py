# Uses python2

def calc_fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return calc_fib(n - 1) + calc_fib(n - 2)


if __name__ == '__main__':
    n = int(input())
    result = calc_fib(n)
    print("Result for ", n, " is ", result)
