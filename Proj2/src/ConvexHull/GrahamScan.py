#!/usr/bin/env python3
import sys


class GrahamScan(object):
    """Find the convex hull given an array of X,Y points using Graham Scan"""

    def __init__(self, points):
        super(GrahamScan, self).__init__()
        self.__points = points

    def calculate(self):
        if len(self.__points) < 4:
            return self.__points

        points = self.__points.copy()
        sorted_by_y = sorted(points, key=lambda point: point[1])
        p0 = sorted_by_y.pop(0)
        sorted_by_polar_angle = self.sort_by_angle(p0, sorted_by_y)
        S = [p0, sorted_by_polar_angle[0], sorted_by_polar_angle[1]]
        for i in range(2, len(sorted_by_polar_angle)):
            while self.ccw(self.next_to_top(S), self.top(S), sorted_by_polar_angle[i]):
                S.pop()
            S.append(sorted_by_polar_angle[i])
        return S

    def sort_by_angle(self, p0, points):
        return sorted(points, key=lambda point: self.angle(point, p0))

    def ccw(self, nt, t, p):
        if nt is None or t is None or p is None:
            return False
        return ((t[0] - nt[0]) * (p[1] - nt[1]) - (t[1] - nt[1]) * (p[0] - nt[0])) <= 0

    def top(self, S):
        if len(S) > 0:
            return S[-1]
        else:
            return None

    def next_to_top(self, S):
        if len(S) > 1:
            return S[-2]
        else:
            return None

    def angle(self, point, p0):
        if (point[1] - p0[1]) == 0:
            return -1 * ((point[0] - p0[0]) / sys.float_info.min)
        else:
            return -1 * (point[0] - p0[0]) / (point[1] - p0[1])
