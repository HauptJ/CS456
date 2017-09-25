#!/usr/bin/env python3
from sorters.Sorter import Sorter
import math

class RadixSort(Sorter):
    """docstring for RadixSort."""

    def __init__(self, A):
        super(RadixSort, self).__init__(A)

# found on the Python Mailing list
# https://mail.python.org/pipermail/python-list/2001-February/094832.html
# slightly modified for my purposes
    def sort(self):
        if(len(self.A) == 0): return []
        B = self.A.copy()
        N = 10
        maxLen = len(str(max(B)))
        # maxLen = 6
        for i in range(maxLen):
            bins = [[] for _ in range(N)]
            for item in B:
                bins[math.floor((item/10**i)%N)].append(item)
            B=[]
            for section in bins:
                B.extend(section)
        return B
