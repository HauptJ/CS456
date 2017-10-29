#!/usr/bin/env python3

class FileWriter(object):
    """Write the results for Project2 to a file"""
    def __init__(self, filename):
        super(FileWriter, self).__init__()
        self.__filename = filename

    def write_line(self, line):
        with open(self.__filename, "a") as f:
            f.write(str(line) + "\n")
        f.close()

    def write_array_of_tuples(self, arr):
        with open(self.__filename, "a") as f:
            for tup in arr:
                st = str(tup[0]) + " " + str(tup[1])
                f.write(st + "\n")
        f.close()
