# Uses python2
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=attrgetter('end'))
    max_right = segments[0].end
    points.append(max_right)
    i = 1
    while i < len(segments):
        if max_right < segments[i].start:
            max_right = segments[i].end
            points.append(max_right)
        i += 1

    return points

if __name__ == '__main__':
    n = int(raw_input())
    data = [0] * (2*n)
    for i in range(n):
        data[2*i], data[2*i+1] = map(int, raw_input().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print str(p) + " ",

