#!/usr/bin/env python3
from Graph.Graph import Graph


class FileReader(object):
    """docstring for FileReader."""

    def __init__(self, file_name):
        super(FileReader, self).__init__()
        self.__file_name = file_name

    def instantiate_graph(self):
        graph = Graph()
        try:
            with open(self.__file_name) as f:
                for line in f:
                    # check if the line defines nodes or edges
                    if line[1] is ':':
                        nodes = line.split(' ')
                        for node in nodes:
                            name = node.split(':')[0]
                            x, y = node.split(':')[1].split(',')
                            graph.add_node(
                                name.strip(), {'X': x.strip(), 'Y': y.strip()})
                    elif line[1] is ',':
                        edges = line.split(' ')
                        for edge in edges:
                            source = edge.split(',')[0]
                            destination, weight = edge.split(',')[1].split(':')
                            graph.add_edge(
                                source.strip(), destination.strip(), weight.strip())
                    else:
                        raise SyntaxError(
                            "Unknown line type in %s" % (this.file_name))
        except Exception as e:
            raise e
        finally:
            f.close()

        return graph
