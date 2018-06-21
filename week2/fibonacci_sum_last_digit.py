# Uses python2
import sys


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

    return sum


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
    print(fibonacci_sum_naive(n))
    print(get_fibonacci_huge(n))
