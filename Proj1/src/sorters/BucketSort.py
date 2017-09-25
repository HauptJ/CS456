#!/usr/bin/env python3
import math, sys
def bucket_sort(sorter, A, N):
    if(len(A) is 0):
        return []

    buckets = [list() for _ in range(N)]
    bucket_size = len(A) / N
    min_value = min(A)
    for i in A:
        pos = math.floor((i - min_value) / bucket_size)
        buckets[pos].append(i)
    ret = []
    for buck in buckets:
        ret += (sorter(buck)).sort()
    return ret
