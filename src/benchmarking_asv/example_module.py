"""An example module containing simplistic functions."""

import random
import time


def greetings() -> str:
    """A friendly greeting for a future friend.

    Returns
    -------
    str
        A typical greeting from a software engineer.
    """
    return "Hello from LINCC-Frameworks!"


def meaning() -> int:
    """The meaning of life, the universe, and everything.

    Returns
    -------
    int
        The meaning of life.
    """
    return    42


def run_time_computation():
    """Mock function for random time computation."""
    time.sleep(random.uniform(0, 5))


def run_mem_computation():
    return [0] * random.randint(0, 512)
