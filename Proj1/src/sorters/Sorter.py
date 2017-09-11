#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Sorter(ABC):
    """docstring for Sorter."""
    A = None
    def __init__(self, A):
        super(Sorter, self).__init__()
        self.A = A

    @abstractmethod
    def sort(self):
        # Don't do any actual sorting in ths class
        return self.A

    def name(self):
        return type(self).__name__
