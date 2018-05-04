# Uses python2
# optimized version of max pairwise product
# instated of iterate through two indices which is O(n^2) get first one then next one alone

n = int(input())
a = [int(x) for x in raw_input().split()]

assert(len(a) == n)

index1 = 1

for i in range(2, n):
    if a[i] > a[index1]:
        index1 = i

if index1 == 1:
    index2 = 2
else:
    index2 = 2

for j in range(1, n):
    if a[j] != a[index1] and a[j] != a[index2]:
        index2 = j

print a[index1] * a[index2]



