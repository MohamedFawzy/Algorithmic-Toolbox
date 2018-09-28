# Uses python2
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    maj_index = 0
    count = 1

    for i in range(1,right):
        if a[maj_index] == a[i]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = i
            count = 1

    for i in range(right):
        if a[i] == a[maj_index]:
            count += 1

    if count > right // 2:
        return a[maj_index]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0] - 1
    a = data[1:]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
