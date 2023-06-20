import os
import time
import psutil
import asyncio
import threading

MAX_ROUND, SHOW_LOG = 10, True

results = []

def log():
  if SHOW_LOG:
    pid = os.getpid()
    thread_name = threading.current_thread().name
    process = psutil.Process(pid)
    memory_info = process.memory_info()
    estimate_memory_usage = memory_info.rss / 1024 / 1024 / 2
    print(f'process: {pid}\t| thread: {thread_name}\t| memory: {estimate_memory_usage:.2f} MB\t| results: {results}')

async def task(x):
  await asyncio.sleep(1)
  results.append(x * x)
  log()

async def run():
  tasks = []
  for x in range(MAX_ROUND):
    tasks.append(asyncio.create_task(task(x)))
  await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(run())
value = sum(results)
print("value: ", value)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
