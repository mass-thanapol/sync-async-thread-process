import os
import time
import psutil
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

def task(x):
  time.sleep(1)
  results.append(x * x)
  log()

def run():
  for x in range(MAX_ROUND):
    task(x)

start_time = time.time()
run()
value = sum(results)
print("value: ", value)
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
