# Uses python2

n = int(input())
a = [int(x) for x in raw_input().split()]

assert(len(a) == n)

product = 0

for i in range(0, n):
    for j in range(i+1, n):
        product = max(product, a[i] * a[j])

print(product)


