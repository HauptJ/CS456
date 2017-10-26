#!/usr/bin/env python3
from math import atan2, floor, pi


class GrahamScan(object):
    """Find the convex hull given an array of X,Y points"""

    def __init__(self, points):
        super(GrahamScan, self).__init__()
        self.__points = points

    def calculate(self):
        points = self.__points
        sorted_by_y = sorted(points, key=lambda point: point[1])
        p0 = sorted_by_y.pop(0)
        sorted_by_polar_angle = self.sort_by_angle(p0, sorted_by_y)
        S = []
        S.append(p0)
        S.append(sorted_by_polar_angle[0])
        S.append(sorted_by_polar_angle[1])
        for i in range(3, len(sorted_by_polar_angle) - 1):
            while self.ccw(self.next_to_top(S), self.top(S), sorted_by_polar_angle[i]):
                S.pop()
            S.append(sorted_by_polar_angle[i])
        return S

    def sort_by_angle(self, p0, points):
        return sorted(points, key=lambda point: (-1 * (point[0] - p0[0]) / (point[1] - p0[1])))

    def ccw(self, nt, t, p):
        if nt == None or t == None or p == None:
            return False
        return ((t[0] - nt[0]) * (p[1] - nt[1]) - (t[1] - nt[1]) * (p[0] - nt[0])) <= 0

    def top(self, S):
        if len(S) > 0:
            return S[len(S) - 1]
        else:
            return None

    def next_to_top(self, S):
        if len(S) > 1:
            return S[len(S) - 2]
        else:
            return None
