# Uses python2
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    portion = [float(v) / float(w) for v, w in zip(values, weights)]
    print(portion)
    return value



if __name__ == "__main__":
    data = list(map(int, raw_input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
