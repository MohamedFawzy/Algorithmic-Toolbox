# Uses python2
import random
import math


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def get_reminder(m):
    previous = 0
    current = 1

    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge(n):
    reminder = n % get_reminder(10)
    result = get_fibonacci(reminder)
    return result


if __name__ == '__main__':
    input = raw_input()
    n = int(input)
    #print(fibonacci_sum_naive(n))
    print(get_fibonacci_huge(n))
    # stress testing
    # while(True):
    #     # run 100 test cases with random numbers between 0, 10 power 14
    #     for _ in range(0,100):
    #         n = random.randrange(0, math.pow(10, 2))
    #         naive_result = fibonacci_sum_naive(n)
    #         good_result  = get_fibonacci_huge(n)
    #         print "Result of naive is ", naive_result, " and for optimized version is ", good_result
    #         if naive_result != good_result:
    #             break

