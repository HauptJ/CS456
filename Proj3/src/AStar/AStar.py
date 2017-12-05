#!/usr/bin/env python3
from PriorityQueue.PriorityQueue import PriorityQueue
from Graph.Graph import Graph
import sys


class AStar(object):
    """docstring for AStar."""

    def __init__(self, graph):
        super(AStar, self).__init__()
        self.__graph = graph

    def get_sortable_tuple(self, node):
        name = node[0]
        value = node[1]['value']
        return (value, {name: node[1]})

    def find_path(self, source, destination):
        self.__graph.set_distance_heuristic(source)
        discovered = PriorityQueue()
        explored = []
        src = self.__graph.get_node(source)
        costs = {source: 0}
        heuristic_costs = {source: self.__graph.get_node(destination)['value']}
        discovered.put((heuristic_costs[source], src))
        dest = self.__graph.get_node(destination)
        path = {}
        while True:
            current = discovered.get()[1]

            if current['name'] == dest['name']:
                return (path, current['name'])

            explored.append(current)

            for neighbor in self.__graph.get_neighbors_of(current):
                if neighbor in explored:
                    continue
                cost = costs[current['name']] + \
                    int(current['edges'][neighbor['name']])
                heuristic_cost = cost + neighbor['value']

                if (heuristic_cost, neighbor) not in discovered:
                    discovered.put((heuristic_cost, neighbor))

                if neighbor['name'] in costs and cost >= costs[neighbor['name']]:
                    continue

                path[neighbor['name']] = {
                    'from': current['name'], 'cost': cost}
                costs[neighbor['name']] = cost
                heuristic_costs[neighbor['name']] = heuristic_costs

        return False, False
