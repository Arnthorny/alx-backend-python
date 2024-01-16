#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n. The
code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine
    """
    l_r = range(n)
    all_tasks = await asyncio.gather(*[task_wait_random(max_delay) for x in
                                       l_r])
    return sorted(all_tasks)
