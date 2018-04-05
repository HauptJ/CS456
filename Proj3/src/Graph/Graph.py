#!/usr/bin/env python3
import math


class Graph(object):
    """docstring for Graph."""

    def __init__(self):
        super(Graph, self).__init__()
        self.__graph = {}
        self.__num_edges = 0
        self.__num_vertices = 0

    def __str__(self):
        string = ""
        string = string + "Graph Size: " + str(self.size()) + "\n"
        for node in self.__graph.items():
            name = str(node[0])
            string = string + "\tName: " + name
            if node[1]['vertex'] is not None:
                string = string + \
                    "\n\tVertex: ( " + str(node[1]['vertex']['X'])
                string = string + " , " + str(node[1]['vertex']['Y']) + " )"
            string = string + "\n\tValue: " + str(node[1]['value'])
            string = string + "\n\tEdges: \n"
            if len(node[1]['edges']) is 0:
                string = string + "\t\tNo Outgoing Edges\n"

            for key in node[1]['edges'].keys():
                string = string + "\t\tEdge: " + name + " -> " + str(key)
                string = string + " Weight: " + str(node[1]['edges'].get(key))
                string = string + "\n"
            string = string + "\n"
        return str(list(self.__graph))

    def __getitem__(self, key):
        if key is None:
            raise Exception("Key is None")
        if key < 0 or key >= self.__num_vertices:
            raise IndexError("Index %s is not in the graph" % index)
        return self.__graph.get(list(self.__graph)[key])

    def get_edges(self):
        edges = []
        for key in self.__graph.keys():
            vertex = self.__graph.get(key)
            for key in vertex['edges'].keys():
                edges.append((vertex['name'], key, vertex['edges'].get(key)))
        return edges

    def get_index_of_node(self, name):
        if name not in self.__graph.keys():
            raise IndexError("Node %s is not in the graph" % name)
        return list(self.__graph).index(name)

    def has_node(self, name):
        return name in self.__graph

    def add_node(self, name, vertex):
        self.__graph[name] = {'name': name,
                              'vertex': vertex, 'value': None, 'edges': {}}
        self.__num_vertices = self.__num_vertices + 1

    def size(self):
        return self.__num_vertices

    def num_edges(self):
        return self.__num_edges

    def add_edge(self, source, destination, weight):
        self.__graph[source]['edges'][destination] = weight
        self.__graph[destination]['edges'][source] = weight
        self.__num_edges = self.__num_edges + 1

    def has_edge(self, source, destination):
        if source not in self.__graph.keys():
            return false

        if destination not in self.__graph.keys():
            return false

        return destination in self.__graph[source]['edges'].keys()

    def get_edge_weight(self, source, destination):
        if not self.has_edge(source, destination):
            return -1

        return self.__graph[source]['edges'][destination]

    def set_node_value(self, node, value):
        if node not in self.__graph.keys():
            return

        self.__graph[node]['value'] = value

    def get_node(self, name):
        if self.has_node(name) is False:
            return -1

        return self.__graph[name]

    def get_node_value(self, node):
        if node not in self.__graph.keys():
            return

        return self.__graph[node]['value']

    def get_names(self):
        return self.__graph.keys()

    def get_nodes(self):
        return list(self.__graph.items())

    def get_neighbors_of(self, node):
        neighbors = []
        for edge in node['edges']:
            neighbors.append(self.get_node(edge))
        return neighbors

    def __distance(self, x1, x2, y1, y2):
        return math.sqrt(math.pow((int(x2) - int(x1)), 2) + math.pow((int(y2) - int(y1)), 2))

    def set_distance_heuristic(self, source):
        src_vertex = self.__graph[source]['vertex']
        for key in self.__graph.keys():
            # ignore source
            if key is source:
                self.__graph[key]['value'] = 0
                continue
            # get the node's vertex
            vertex = self.__graph[key]['vertex']
            # get the distance between the vertices
            distance = self.__distance(
                src_vertex['X'], vertex['X'], src_vertex['Y'], vertex['Y'])
            # set the nodes value to the distance
            self.__graph[key]['value'] = distance
