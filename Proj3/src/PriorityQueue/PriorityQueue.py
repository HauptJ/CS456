#!/usr/bin/env python3
from heapq import heappush, heappop
import queue

class PriorityQueue(queue.PriorityQueue):
    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)

    def __contains__(self, item):
        with self.mutex:
            for iq in self.queue:
                if item[1]['name'] == iq[1]['name']:
                    return True
            return False

    def remove(self, item):
        with self.mutex:
            for iq in self.queue:
                if item[1]['name'] == iq[1]['name']:
                    self.queue.remove(iq)
                    break

    def __len__(self):
        with self.mutex:
            return len(self.queue)
