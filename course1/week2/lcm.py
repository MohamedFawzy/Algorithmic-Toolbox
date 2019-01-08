# Uses python2
# LCM(a,b) * GCD(a,b)
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a, b):
    if b == 0:
        return a

    a_reminder = a % b

    return gcd(b, a_reminder)

def lcm(a, b):
    return (a*b) // gcd(a,b)


if __name__ == '__main__':
    input = raw_input()
    a, b = map(int, input.split())
    print(lcm(a, b))

