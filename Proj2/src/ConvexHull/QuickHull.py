#!/usr/bin/env python3
import sys, math

class QuickHull(object):
    """docstring for QuickHull."""
    def __init__(self, points):
        super(QuickHull, self).__init__()
        self.__points = points

    def calculate(self):
        points = self.__points.copy()
