#!/usr/bin/env python3


class JarvisMarch(object):
    """Find the convex hull given an array of X,Y points using JarvisMarch"""

    def __init__(self, points):
        super(JarvisMarch, self).__init__()
        self.__points = points

    def calculate(self):
        if len(self.__points) < 4:
            return self.__points
        points = self.__points.copy()
        # sort the points by lowest X value
        sorted_by_x = sorted(points, key=lambda point: point[0])
        # get the lowest X point
        current = sorted_by_x[0]
        endpoint = None
        hull = [current]
        while endpoint != hull[0]:
            endpoint = sorted_by_x[0]
            for j in range(1, len(sorted_by_x)):
                if (endpoint == current) or (self.is_left_of_line(current, endpoint, sorted_by_x[j])):
                    endpoint = sorted_by_x[j]
                    # replace the previous point if they are colinear
                    if len(hull) >= 2 and self.is_colinear(self.next_to_top(hull), self.top(hull), endpoint):
                        hull.pop()
            current = endpoint
            hull.append(current)
        return hull

    def is_left_of_line(self, A, B, C):
        return ((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])) > 0

    def is_colinear(self, A, B, C):
        return ((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])) == 0

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
