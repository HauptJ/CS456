#!/usr/bin/env python3
import sys
from FileIO.FileImporter import FileImporter
from ConvexHull.GrahamScan import GrahamScan

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify an input file")
        exit(1)
    filename = sys.argv[1]
    # get the points from a file
    points = (FileImporter(filename)).get_array()
    # calculate graham scan convex hull
    print((GrahamScan(points.copy())).calculate())
