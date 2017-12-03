#!/usr/bin/env python3
from Graph.Graph import Graph
import sys


class FloydWarshall(object):
    """docstring for FloydWarshall."""

    def __init__(self, graph):
        super(FloydWarshall, self).__init__()
        self.__graph = graph
        self.__dist = None
        self.__next = None
        self.__shortestPath()

    def find_path(self, source, destination):
        u = self.__graph.get_index_of_node(source)
        v = self.__graph.get_index_of_node(destination)
        if self.__next[u][v] is None:
            return ([], 0)

        path = [self.__graph[u]]
        total_cost = 0
        while u is not v:
            curr = self.__graph[u]
            w = curr["edges"][self.__graph[self.__next[u][v]]["name"]]
            total_cost = total_cost + int(w)
            u = self.__next[u][v]
            path.append(self.__graph[u])
        return (path, total_cost)

    def __shortestPath(self):
        num_vertices = self.__graph.size()
        num_edges = self.__graph.num_edges()
        self.__dist = [[sys.maxsize for _ in range(num_vertices)]
                       for _ in range(num_vertices)]
        self.__next = [[None for _ in range(num_vertices)]
                       for _ in range(num_vertices)]

        for i in range(num_vertices):
            self.__dist[i][i] = 0

        for edge in self.__graph.get_edges():
            u = self.__graph.get_index_of_node(edge[0])
            v = self.__graph.get_index_of_node(edge[1])
            w = int(edge[2])
            self.__dist[u][v] = w
            self.__next[u][v] = v

        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if self.__dist[i][j] > self.__dist[i][k] + self.__dist[k][j]:
                        self.__dist[i][j] = self.__dist[i][k] + \
                            self.__dist[k][j]
                        self.__next[i][j] = self.__next[i][k]
