#!/usr/bin/env python3

from collections import deque
from sys import argv

EXEC_RU = "ra"
EXEC_RD = "rra"
EXEC_PA = "pa"
EXEC_PB = "pb"

class PushSwap:
    def __init__(self, value):
        self.stack = []
        self.container = []
        self.sorted = []
        self.found = 0
        self.execs = []
        for v in value.split():
            if not v.isnumeric():
                raise SystemError("Not an int")
            v = int(v)
            self.stack.append(v)
            self.sorted.append(v)
        self.sorted.sort()

    def sa(self):
        if len(self.stack) > 1:
            t = self.stack[0]
            self.stack[0] = self.stack[1]
            self.stack[1] = t

    def sb(self):
        if len(self.container) > 1:
            t = self.container[0]
            self.container[0] = self.container[1]
            self.container[0] = t

    def ss(self):
        self.sa()
        self.sb()

    def pa(self):
        if len(self.container) > 0:
            self.stack.append(self.container.pop())

    def pb(self):
        if len(self.stack) > 0:
            self.container.append(self.stack.pop())

    def ra(self):
        if len(self.stack) > 1:
            self.stack = self.stack[-1:] + self.stack[:-1]

    def rb(self):
        if len(self.container) > 1:
            self.container = self.container[-1:] + self.container[:-1]

    def rr(self):
        self.ra()
        self.rb()

    def rra(self):
        if len(self.stack) > 1:
            self.stack = self.stack[1:] + self.stack[:1]

    def rrb(self):
        if len(self.container) > 1:
            self.container = self.container[1:] + self.container[:1]
            
    def rrr(self):
        self.rra()
        self.rrb()

    def sort(self):
        while len(self.stack) > 0:
            self.sort2()
        for _ in range(len(self.sorted)):
            self.pa()
        for v in self.execs:
            for _ in range(v[1]):
                print(v[0])
            print(EXEC_PB)
        for _ in range(len(self.sorted)):
            print(EXEC_PA)

    def sort2(self):
        i = self.stack.index(self.sorted[self.found])
        a = i + 1
        b = len(self.sorted) - i
        if a < b:
            self.execs.append((EXEC_RU, a))
            for _ in range(a):
                self.rra()
        else:
            self.execs.append((EXEC_RD, b))
            for _ in range(b):
                self.ra()
        self.pb()
        self.found += 1

if __name__ == "__main__":
    ps = PushSwap(" ".join(argv[1:]))
    ps.sort()
