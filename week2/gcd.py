# Uses python2

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd(a, b):
    if b == 0:
        return a

    a_reminder = a % b

    return gcd(b, a_reminder)

if __name__ == "__main__":
    input = raw_input()
    a, b = map(int, input.split())
    print(gcd(a, b))
