#!/usr/bin/env python3
import sys
sys.path.append("..")

from unittest import TestCase

from sorters.RadixSort import RadixSort
from sorters.BucketSort import bucket_sort


class TestBubbleSort(TestCase):

    def test_it_sorts_an_empty_array(self):
        # given an empty array
        A = []
        C = bucket_sort(RadixSort, A, 10)
        # and check if the array is <sorted></sorted>
        self.assertEqual(C, A)

    def test_it_sorts_an_unsorted_array(self):
        # given an unsorted array
        A = [9, 5, 0, 2, 3, 15, 35]
        # and a bubble sort instance
        C = bucket_sort(RadixSort, A, len(A))
        # and check if the array is sorted
        self.assertEqual(C, sorted(A))

    def test_it_sorts_an_reverse_sorted_array(self):
        # given a reverse sorted array
        A = [35, 15, 9, 5, 3, 2, 0]
        # and a bubble sort instance
        C = bucket_sort(RadixSort, A, len(A))
        # and check if the array is sorted
        self.assertEqual(C, sorted(A))

    def test_it_sorts_an_unsorted_array_with_duplicates(self):
        # given an unsorted array
        A = [9, 5, 0, 2, 3, 15, 35, 9]
        # and a bubble sort instance
        C = bucket_sort(RadixSort, A, len(A))
        # and check if the array is sorted
        self.assertEqual(C, sorted(A))

    def test_it_sorts_an_unsorted_array_with_duplicates_and_N_is_not_full_length(self):
        # given an unsorted array
        A = [9, 5, 0, 2, 3, 15, 35, 9]
        # and a bubble sort instance
        C = bucket_sort(RadixSort, A, int(len(A) / 2))
        # and check if the array is sorted
        self.assertEqual(C, sorted(A))
