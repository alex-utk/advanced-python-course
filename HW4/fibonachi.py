import numpy as np
from time import time
from multiprocessing import Process
from threading import Thread

def fibonachi(n):
    if n in [0, 1]:
        return n
    else:
        a = 0
        b = 1
        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c
    
if __name__ == '__main__':
    n = 200000
    
    process_all = []
    treads_all = []
    
    for _ in range(10):
        start = time()
        process_list = [Process(target=fibonachi, args=(n, )) for _ in range(10)]
        for process in process_list:
            process.start()
            
        for process in process_list:
            process.join()
        end = time()
        process_all.append(end-start)

        ####
        start = time()
        thread_list = [Thread(target=fibonachi, args=(n, )) for _ in range(10)]
        for thread in thread_list:
            thread.start()
            
        for thread in thread_list:
            thread.join()
        end = time()
        treads_all.append(end-start)
        
    process_avg = np.array(process_all).mean()
    treads_avg = np.array(treads_all).mean()
    
    print(process_all)
    print(f'process average = {process_avg}')
    print()
    print(treads_all)
    print(f'treads average = {treads_avg}')
    
    print(f'\nРазница в {treads_avg / process_avg} раз')