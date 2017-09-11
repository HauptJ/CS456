#!/usr/bin/env python3
from sorters.Sorter import Sorter

class BubbleSort(Sorter):
    """docstring for BubbleSort."""
    def __init__(self, A):
        super(BubbleSort, self).__init__(A)

    def sort(self):
        B = self.A.copy()
        n = len(B)
        while n is not 0:
            newn = 0
            for i in range(1, n):
                if B[i - 1] > B[i]:
                    x = B[i]
                    B[i] = B[i - 1]
                    B[i - 1] = x
                    newn = i
            n = newn
        return B
