#!/usr/bin/env python3
from sorters.Sorter import Sorter


class QuickSort(Sorter):
    """docstring for QuickSort."""

    def __init__(self, A):
        super(QuickSort, self).__init__(A)

    def sort(self):
        B = self.A.copy()
        self.quicksort(B, 0, len(B) - 1)
        return B

    def quicksort(self, A, p, r):
        if p < r:
            q = self.partition(A, p, r)
            self.quicksort(A, p, q - 1)
            self.quicksort(A, q + 1, r)

    def partition(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i = i + 1
                temp = A[j]
                A[j] = A[i]
                A[i] = temp
        temp = A[i + 1]
        A[i + 1] = A[r]
        A[r] = temp
        return i + 1
