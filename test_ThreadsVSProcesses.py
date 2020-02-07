import multiprocessing
import threading
import time
import sys

if __name__ == '__main__':
    cpu_n_iters = int(sys.argv[1])
    sleep = 1
    cpu_count = multiprocessing.cpu_count()
    input_params = [
        (CpuThread, cpu_n_iters),
        (CpuProcess, cpu_n_iters),
        (IoThread, sleep),
        (IoProcess, sleep),
    ]
    header = ['nthreads']
    for thread_class, _ in input_params:
        header.append(thread_class.__name__)
    print(' '.join(header))
    for nthreads in range(1, 2 * cpu_count):
        results = [nthreads]
        for thread_class, work_size in input_params:
            start_time = time.time()
            threads = []
            for i in range(nthreads):
                thread = thread_class(work_size)
                threads.append(thread)
                thread.start()
            for i, thread in enumerate(threads):
                thread.join()
            results.append(time.time() - start_time)
        print(' '.join('{:.6e}'.format(result) for result in results))
