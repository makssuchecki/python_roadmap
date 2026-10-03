# Global Interpreter Lock or GIL is a mutex that allows only one thread to hold
# the control of the Python interpreter
# This means that only one thread can be in a state of execution at any point in time

from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == "__main__":
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)

