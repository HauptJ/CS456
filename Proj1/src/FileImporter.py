#!/usr/bin/env python3

class FileImporter(object):
    """docstring for FileImporter."""
    def __init__(self, filename):
        super(FileImporter, self).__init__()
        self.filename = filename

    def get_array(self):
        arr = []
        with open(self.filename) as f:
            for line in f:
                arr.append(int(line.rstrip()))
            f.close()
        return arr
