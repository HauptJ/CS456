#!/usr/bin/env python3


class FileImporter(object):
    """Reads an array of X,Y points from filename."""

    def __init__(self, filename):
        super(FileImporter, self).__init__()
        self.__filename = filename

    def get_array(self):
        arr = []
        with open(self.__filename) as f:
            for line in f:
                x, y = line.split(' ')
                arr.append((int(x), int(y)))
            f.close()
        return arr
