import time


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """

    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        time.sleep(0.5)

    def time_iterkeys(self):
        time.sleep(0.01)

    def time_range(self):
        time.sleep(0.25)

    def time_xrange(self):
        time.sleep(1)


class MemSuite:
    def mem_list(self):
        return [0] * 255
