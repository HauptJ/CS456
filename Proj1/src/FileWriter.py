#!/usr/bin/env python3

class FileWriter(object):
    """docstring for FileWriter."""
    sort_size = None
    buckets = None
    bubble_sort = None
    quick_sort = None
    radix_sort = None
    arr = []
    string_io = None

    def __init__(self, filename):
        super(FileWriter, self).__init__()
        self.filename = filename

    def set_number_buckets(self, buckets):
        self.buckets = buckets
        return self

    def set_sort_size(self, sort_size):
        self.sort_size = sort_size
        return self

    def set_bubble_sort_time(self, bubble_sort):
        self.bubble_sort = bubble_sort
        return self

    def set_quick_sort_time(self, quick_sort):
        self.quick_sort = quick_sort
        return self

    def set_radix_sort_time(self, radix_sort):
        self.radix_sort = radix_sort
        return self

    def set_out_array(self, arr):
        self.arr = arr
        return self

    def set_file_out(self, out):
        self.string_io = out

    def write(self):
        if self.string_io is not None:
            self.string_io.write("Sort Size: " + str(self.sort_size) + "\n")
            self.string_io.write("Number of Buckets: " + str(self.buckets) + "\n")
            if self.bubble_sort is not None:
                self.string_io.write("Bubble Sort: " + str(self.bubble_sort) + "s\n")
            if self.quick_sort is not None:
                self.string_io.write("Quick Sort: " + str(self.quick_sort) + "s\n")
            if self.radix_sort is not None:
                self.string_io.write("Radix Sort: " + str(self.radix_sort) + "s\n")
            for i in self.arr:
                self.string_io.write(str(i) + "\n")
        else:
            with open(self.filename, 'w+') as f:
                f.write("Sort Size: " + str(self.sort_size) + "\n")
                f.write("Number of Buckets: " + str(self.buckets) + "\n")
                if self.bubble_sort is not None:
                    f.write("Bubble Sort: " + str(self.bubble_sort) + "s\n")
                if self.quick_sort is not None:
                    f.write("Quick Sort: " + str(self.quick_sort) + "s\n")
                if self.radix_sort is not None:
                    f.write("Radix Sort: " + str(self.radix_sort) + "s\n")
                for i in self.arr:
                    f.write(str(i) + "\n")
                f.close()
