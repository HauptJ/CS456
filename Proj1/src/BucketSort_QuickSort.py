#!/usr/bin/env python3
import math
import sys
from sorters.QuickSort import QuickSort

def bucket_sort_quick(A, N):
    if(len(A) is 0):
        return []

    buckets = [list() for _ in range(N)]
    for i in A:
        pos = (math.floor(i/2**(sys.getsizeof(i)-N)))
        buckets[pos].append(i)
    ret = []
    for buck in buckets:
        ret += (QuickSort(buck)).sort()
    return ret
