#!/usr/bin/env python3
import os
import time
import sys
from sorters.BubbleSort import BubbleSort
from sorters.RadixSort import RadixSort
from sorters.QuickSort import QuickSort
from sorters.BucketSort import bucket_sort
from FileImporter import FileImporter
from FileWriter import FileWriter
from os.path import basename
from multiprocessing.pool import ThreadPool


def bubble_sort_thread(arr, bucket_size):
    start_time = time.clock()
    ret = bucket_sort(BubbleSort, arr, bucket_size)
    end_time = time.clock()
    return end_time - start_time


if __name__ == '__main__':
    # begin execution

    if len(sys.argv) < 3:
        print("Not enough paramaters")
        exit(1)

    bucket_size = int(sys.argv[1])
    input_file_name = str(sys.argv[2])
    output_file_name = "owens-" + \
        os.path.splitext(basename(input_file_name))[
            0] + "-" + str(bucket_size) + ".txt"
    fw = FileWriter(output_file_name)
    fi = FileImporter(input_file_name)
    arr = fi.get_array()

    # Bubble Sort Threads
    pool = ThreadPool(processes=3)
    pool_results = []
    for i in range(3):
        print("Starting bucket sort thread " + str(i))
        pool_results.append(pool.apply_async(
            bubble_sort_thread, (arr, bucket_size)))

    # End Bubble Sort Threads

    # Quick Sort
    start_times = []
    end_times = []
    for i in range(3):
        print("Starting quick sort " + str(i))
        start_times.append(time.clock())
        ret = bucket_sort(QuickSort, arr, bucket_size)
        end_times.append(time.clock())

    quick_sort_time = (sum(end_times) - sum(start_times)) / len(end_times)
    
    # End Quick Sort

    # Radix Sort
    start_times = []
    end_times = []
    for i in range(3):
        print("Starting radix sort " + str(i))
        start_times.append(time.clock())
        ret = bucket_sort(RadixSort, arr, bucket_size)
        end_times.append(time.clock())
        
    radix_sort_time = (sum(end_times) - sum(start_times)) / len(end_times)
    
    # End Radix Sort

    # Bubble Sort Thread Joins
    bubble_sort_time = 0
    for i in range(len(pool_results)):
        print("Waiting for bubble sort thread " + str(i))
        bubble_sort_time = (bubble_sort_time + pool_results[i].get()) / len(pool_results)
    # End Bubble Sort Thread Joins

    fw = fw.set_number_buckets(bucket_size).set_sort_size(
        len(ret)).set_quick_sort_time(quick_sort_time)
    fw.set_bubble_sort_time(bubble_sort_time).set_radix_sort_time(
        radix_sort_time).set_out_array(ret).write()
