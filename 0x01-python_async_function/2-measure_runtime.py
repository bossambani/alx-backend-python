#!/usr/bin/env python3
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
"""
function with integers n and max_delay as arguments
that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns total_time / n as a float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
