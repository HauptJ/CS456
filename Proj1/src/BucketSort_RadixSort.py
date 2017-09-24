#!/usr/bin/env python3
import math
import sys
from sorters.RadixSort import RadixSort

def bucket_sort_radix(A, N):
    if(len(A) is 0):
        return []

    buckets = [list() for _ in range(N)]
    for i in range(N):
        pos = (math.floor(i/2**(sys.getsizeof(i)-N)))
        buckets[pos].append(A[i])
    ret = []
    for buck in buckets:
        ret += (RadixSort(buck)).sort()
    return ret
