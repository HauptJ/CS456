#!/usr/bin/env python3
import sys
import os
sys.path.append("..")

from unittest import TestCase

from FileImporter import FileImporter

class TestFileImporter(TestCase):

    def test_it_creates_an_array_from_a_file(self):
        # given a file
        filename = os.getcwd() + '/10.txt'
        # and a file importer
        file_importer = FileImporter(filename)
        # get an array from the file
        arr = file_importer.get_array()
        # check the size of the array
        self.assertEqual(len(arr), 10)
        # check if the values are in the array
        self.assertEqual(arr, [17, 63, 31, 95, 51, 38, 30, 22, 33, 83])
