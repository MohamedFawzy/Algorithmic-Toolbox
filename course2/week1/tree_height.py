# python3

import sys
import threading


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.nodes = {}

        for i in range(self.n):
            self.nodes[i] = []

        for i in range(self.n):
            if self.parent[i] == -1:
                pass
            else:
                self.nodes[self.parent[i]] += [i]

    def compute_height(self):
        root = None
        try:
            root = self.parent.index(-1)
        except ValueError:
            return 0
        queue = []
        queue.append(root)
        height = 0

        while True:
            node_count = len(queue)
            if node_count == 0:
                return height
            height += 1

            while node_count > 0:
                node = queue[0]
                queue.pop(0)
                if self.nodes[node]:
                    for v in self.nodes[node]:
                        queue.append(v)
                node_count -= 1


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
