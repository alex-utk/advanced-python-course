import math
import multiprocessing
from typing import Literal
import time
import itertools
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging
import multiprocessing_logging

multiprocessing_logging.install_mp_handler() # мультипроцессорный логгер

def split_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""
    formatter = logging.Formatter('%(asctime)s  %(message)s')

    handler = logging.FileHandler(log_file, mode='w')        
    handler.setFormatter(formatter)


    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


def inner_func(f, arg, logg):
    logg.info(f'Started {arg[0]} - {arg[-1]}')
    
    res = sum([f(a) * step for a in arg])
    
    logg.info(f'Started {arg[0]} - {arg[-1]}')
    return res


def integrate(f, a, b, *, log, n_jobs=1,
              job_type: Literal['thread', 'process']='process',
              n_iter=100000):# 10000000  400000  100
    step = (b - a) / n_iter
    steps = [a + i * step for i in range(n_iter)]
    batches = list(split_list(steps, 100))
    
    if job_type == 'thread':
        with ThreadPoolExecutor(max_workers=n_jobs) as executor:
            results = executor.map(inner_func, [f] * len(batches), batches, [log] * len(batches))
    else:
        with ProcessPoolExecutor(max_workers=n_jobs) as executor:
            results = executor.map(inner_func, [f] * len(steps), steps, [log] * len(steps))

    result = sum(results)

    return result


if __name__ == '__main__':    
    setup_logger('tr_logger', 'tr_logger.log')
    setup_logger('pr_logger', 'pr_logger.log')
    
    tr_logger = setup_logger('tr_logger', 'tr_logger.log')
    pr_logger = setup_logger('pr_logger', 'pr_logger.log')
    
    multiprocessing_logging.install_mp_handler(pr_logger) # мультипроцессорный логгер
    
    thread_results = []
    process_results = []
    print('Processes')
    for jobs in range(1, multiprocessing.cpu_count() + 1):
        pr_logger.info(f'!!!!{jobs} PROCESSES!!!!')
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, log=pr_logger, n_jobs=jobs, job_type='process')
        end = time.time()
        process_results.append(end-start)
        print(end-start)
    print('Threads')
    for jobs in range(1, multiprocessing.cpu_count() + 1):
        pr_logger.info(f'!!!!{jobs} THREADS!!!!')
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, log=tr_logger, n_jobs=jobs, job_type='thread')
        end = time.time()
        thread_results.append(end-start)
        print(end-start)
    print()
    print(process_results)
    print(thread_results)
