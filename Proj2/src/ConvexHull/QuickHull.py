#!/usr/bin/env python3


class QuickHull(object):
    """Find the convex hull given an array of X,Y points using QuickHull"""

    def __init__(self, points):
        super(QuickHull, self).__init__()
        self.__points = points

    def calculate(self):
        if len(self.__points) < 4:
            return self.__points
        points = self.__points.copy()
        sorted_by_x = sorted(points, key=lambda point: point[0])
        # find the min and max X points
        min_x = sorted_by_x[0]
        max_x = sorted_by_x[-1]
        # Find the ConvexHull points for the left and right subsets
        # and add them to the hull
        Hull = self.findHull(points, min_x, max_x)
        Hull.extend(self.findHull(points, max_x, min_x))
        return Hull[1:] + Hull[:1]

    def findHull(self, subset, min_x, max_x):
        if max_x == [None] or min_x == [None]:
            return subset
        points_left_of_line = self.divide_into_subsets(min_x, max_x, subset)

        ptC = self.point_max_from_line(min_x, max_x, points_left_of_line)

        if len(ptC) < 1:
            return [max_x]

        points = self.findHull(points_left_of_line, min_x, ptC)
        points = points + self.findHull(points_left_of_line, ptC, max_x)
        return points

    def divide_into_subsets(self, end_A, end_B, points):
        return list(filter(lambda val: self.is_left_of_line(end_A, end_B, val), points))

    def point_max_from_line(self, min_x, max_x, subset):
        max_point = []
        max_area = None
        for point in subset:
            area = abs((min_x[0] - point[0]) * (max_x[1] - min_x[1]) -
                       (min_x[0] - max_x[0]) * (point[1] - min_x[1])) / 2
            if len(max_point) == 0 or area > max_area:
                max_area = area
                max_point = point
        return max_point

    def is_left_of_line(self, A, B, C):
        if type(A) is list:
            if len(A) > 0:
                A = A.pop()
            else:
                return False
        if type(B) is list:
            if len(B) > 0:
                B = B.pop()
            else:
                return False
        if type(C) is list:
            if len(C) > 0:
                C = C.pop()
            else:
                return False

        return ((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])) > 0

    def is_right_of_line(self, A, B, C):
        return ((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])) < 0
