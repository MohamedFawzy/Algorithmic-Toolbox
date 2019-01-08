# Uses python2

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci(n):
    if n<=1:
        return n

    previous =0
    current =1

    for _ in range(n -1):
        previous, current = current, previous+current

    return current

def get_reminder(m):

     previous =0
     current = 1

     for i in range(m * m +1):
         previous, current = current, (previous + current) % m
         if previous==0 and current==1:
             return i +1



def get_fibonacci_huge(n, m):
    remainder = n % get_reminder(m)
    result = get_fibonacci(remainder) % m
    return result

if __name__ == '__main__':
    input = raw_input();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
