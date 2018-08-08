# Uses python2
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # map values and weights then divide them to get the portion per unit.
    portion = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in xrange(len(weights)+1):
        if capacity == 0:
            return value
            break

        max_w = max(portion)
        index = portion.index(max_w)
        portion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_w
        weights[index] -= add_capacity
        capacity -= add_capacity


    return value



if __name__ == "__main__":
    data = list(map(int, raw_input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
