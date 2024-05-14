import math
import multiprocessing
from typing import Literal
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging
import multiprocessing_logging


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""
    formatter = logging.Formatter('%(asctime)s  %(message)s')

    handler = logging.FileHandler(log_file, mode='w')        
    handler.setFormatter(formatter)


    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger


def inner_func(f, x, step, logg):
    logg.info(f'Started {x}')
    res = f(x) * step
    logg.info(f'Ended {x}')
    return res


def integrate(f, a, b, *, log, n_jobs=1,
              job_type: Literal['thread', 'process']='process',
              n_iter=5000000):
    step_size = (b - a) / n_iter
    steps = [a + i * step_size for i in range(n_iter)]
    
    if job_type == 'thread':
        with ThreadPoolExecutor(max_workers=n_jobs) as executor:
            results = executor.map(inner_func, [f] * len(steps), steps,
                                   [step_size] * len(steps), [log] * len(steps))
    else:
        with ProcessPoolExecutor(max_workers=n_jobs) as executor:
            # chunksize критичен, иначе будет работать очень медленно
            results = executor.map(inner_func, [f] * len(steps), steps,
                                   [step_size] * len(steps), [log] * len(steps), chunksize=1500)

    return sum(results)


if __name__ == '__main__':      
    tr_logger = setup_logger('tr_logger', 'tr_logger.log')
    pr_logger = setup_logger('pr_logger', 'pr_logger.log')
    
    multiprocessing_logging.install_mp_handler(pr_logger) # мультипроцессорный логгер
    
    thread_results = []
    process_results = []
    print('Processes')
    for jobs in range(1, 2*multiprocessing.cpu_count()):
        pr_logger.info(f'!!!!{jobs} PROCESSES!!!!')
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, log=pr_logger, n_jobs=jobs, job_type='process')
        end = time.time()
        process_results.append(end-start)
    print('Threads')
    for jobs in range(1, 2*multiprocessing.cpu_count()):
        pr_logger.info(f'!!!!{jobs} THREADS!!!!')
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, log=tr_logger, n_jobs=jobs, job_type='thread')
        end = time.time()
        thread_results.append(end-start)
    print()
    print(process_results)
    print(thread_results)
