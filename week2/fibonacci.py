# Uses python2

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


if __name__ == '__main__':
    n = int(input())
    result = calc_fib(n)
    print("Result for ", range(n-1), " is ", result)
