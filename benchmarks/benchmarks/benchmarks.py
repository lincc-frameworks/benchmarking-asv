import random
import time

import benchmarking_asv as bench


class TimeSuite:
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        bench.example_module.run_time_computation()

    def time_iterkeys(self):
        bench.example_module.run_time_computation()

    def time_range(self):
        bench.example_module.run_time_computation()

    def time_xrange(self):
        bench.example_module.run_time_computation()


class MemSuite:
    def mem_list(self):
        return bench.example_module.run_mem_computation(. )
