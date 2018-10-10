# Uses python2
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, raw_input().split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))

