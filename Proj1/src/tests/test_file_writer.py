#!/usr/bin/env python3
import sys
import os
from io import StringIO
sys.path.append("..")

from unittest import TestCase

from FileWriter import FileWriter

class TestFileWriter(TestCase):

    def test_it_writes_buble_sort_data_to_a_file(self):
        # given a file
        filename = os.getcwd() + 'bubble_out.txt'
        # and a stringIO
        out = StringIO()
        # and the data
        sort_size = 10
        number_of_buckets = 2
        bubble_sort_time = 0.0071
        sorted_array = [17, 22, 30, 31, 33, 38, 51, 63, 83, 95]
        # and the FileWriter
        fw = FileWriter(filename)
        # now override the file write
        fw.set_file_out(StringIO())
        # write the data
        fw.set_sort_size(sort_size).set_number_buckets(number_of_buckets).set_bubble_sort_time(bubble_sort_time).set_out_array(sorted_array).write()
        # now get the file
        out.seek(0)
        content = out.readline()
