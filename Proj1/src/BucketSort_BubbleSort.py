#!/usr/bin/env python3
import os
import time
import sys
from sorters.BubbleSort import BubbleSort
from sorters.BucketSort import bucket_sort
from FileImporter import FileImporter
from FileWriter import FileWriter
from os.path import basename

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
    start_times = []
    end_times = []
    for _ in range(3):
        start_times.append(time.clock())
        ret = bucket_sort(BubbleSort, arr, bucket_size)
        end_times.append(time.clock())

    bubble_sort_time = sum(end_times) - sum(start_times)

    fw = fw.set_number_buckets(bucket_size).set_sort_size(
        len(ret)).set_bubble_sort_time(bubble_sort_time)
    fw.set_out_array(ret).write()
