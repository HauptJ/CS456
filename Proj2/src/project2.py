#!/usr/bin/env python3
import sys
import time
from FileIO.FileWriter import FileWriter
from ConvexHull.QuickHull import QuickHull
from multiprocessing.pool import ThreadPool
from FileIO.FileImporter import FileImporter
from ConvexHull.GrahamScan import GrahamScan
from ConvexHull.JarvisMarch import JarvisMarch


def graham_scan(points):
    start_time = time.clock()
    hull = (GrahamScan(points.copy())).calculate()
    end_time = time.clock()
    return (hull, end_time - start_time)


def jarvis_march(points):
    start_time = time.clock()
    hull = (JarvisMarch(points.copy())).calculate()
    end_time = time.clock()
    return (hull, end_time - start_time)


def quick_hull(points):
    start_time = time.clock()
    hull = (QuickHull(points.copy())).calculate()
    end_time = time.clock()
    return (hull, end_time - start_time)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify an input file")
        exit(1)
    filename = sys.argv[1]
    # get the points from a file
    points = (FileImporter(filename)).get_array()
    # get count of points
    count_point = len(points)
    # get a thread pool
    pool = ThreadPool(processes=3)
    # get quick hull time
    print("Starting QuickHull")
    quick_hull_results = quick_hull(points)
    # get jarvis march time
    print("Starting JarvisMarch")
    jarvis_march_results = jarvis_march(points)
    # get quick hull time
    print("Starting GrahamScan")
    graham_scan_results = graham_scan(points)
    # set the output file name
    out_filename = str(count_point) + ".txt"
    # get a file writer
    fw = FileWriter(out_filename)
    # write ConvexHull calculation times
    fw.write_line("Graham: " + format(graham_scan_results[1], '0.7f') + " sec")
    fw.write_line("Jarvis: " + format(jarvis_march_results[1], '0.7f') + " sec")
    fw.write_line("Quick: " + format(quick_hull_results[1], '0.7f') + " sec")
    # write the ConvexHull
    fw.write_array_of_tuples(graham_scan_results[0])
