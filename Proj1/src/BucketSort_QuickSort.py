#!/usr/bin/env python3
import math
from sorters.QuickSort import quick_sort

def bucket_sort_quick(A):
    B = []
    C = []
    n = len(A)
    for i in range(0, n-1):
        B.append([])
    for x in range(1, n):
        pass
    for i in range(0, n-1):
        quick_sort(B[i])
    for l in B:
        C.append(l)
    return C

A = []
for x in range(50):
    A.append(50 - x - 1)

bucket_sort_quick(A)
