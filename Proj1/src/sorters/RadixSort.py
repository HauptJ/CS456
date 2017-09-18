#!/usr/bin/env python3
from sorters.Sorter import Sorter
import math

class RadixSort(Sorter):
    """docstring for RadixSort."""

    def __init__(self, A):
        super(RadixSort, self).__init__(A)

    def sort(self):
        if(len(self.A) == 0): return []
        B = self.A.copy()
        number_digits = len(str(max(B)))
        return self.__radix_sort(B, 10, number_digits)

    def __radix_sort(self, ARR, N, MAXLEN):
        RADIX = 1
        for i in range(MAXLEN):
            bins = [[] for _ in range(N)]
            for item in ARR:
                # Item / RADIX to the power i, modulus give the specific bin
                # Moves the currently considered digit over
                bins[math.floor((item/RADIX ** i)%N)].append(item)
            RADIX = RADIX * 10
            ARR=[]
            for section in bins:
                ARR.extend(section)
        return ARR
