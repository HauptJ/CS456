#!/usr/bin/env python3

from FloydWarshall.FloydWarshall import FloydWarshall
from FileIO.FileReader import FileReader
import sys


def print_path(path):
    cost = path[1]
    path = path[0]
    if len(path) is 0:
        print("A path does not exist")
    p = str(path[0]['name'])
    for i in range(1, len(path)):
        p = p + " -> " + str(path[i]['name'])
    print(p)
    print("Number of points in the path is: " + str(len(path)))
    print("The Total cost is: " + str(cost))


if __name__ == '__main__':
    # If no filename was provided
    if len(sys.argv) < 2:
        print("Please specify an input file")
        exit(1)
    # get filename from program arguments
    filename = sys.argv[1]
    # generate a graph from the file
    try:
        graph = (FileReader(filename)).instantiate_graph()
    except Exception as e:
        print("Unable to use the input file: " + str(e))
        sys.exit(1)

    # A Star object
    pathfinder = FloydWarshall(graph)
    # should exit?
    exit = False
    while(exit is not True):
        # ask user for source and destination
        source = input("Enter a source node (or 'Q' to quit): ")
        # check if the user wants to quit
        if source is 'Q':
            exit = True
            continue
        # check that the source exists
        if graph.has_node(str(source.strip())) is False:
            print("Graph does not have that source")
            continue

        destination = input("Enter a destination node (or 'Q' to quit): ")
        # check if the user wants to quit
        if destination is 'Q':
            exit = True
            continue
        # check that the destination exists
        if graph.has_node(str(destination.strip())) is False:
            print("Graph does not have that destination")
            continue
        # get a path given the source and destination
        path = pathfinder.find_path(source.strip(), destination.strip())
        # print the path
        print("For point " + str(source) + " to point " + str(destination))
        print_path(path)

    print("Quiting")
