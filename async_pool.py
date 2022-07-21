import multiprocessing
import time
from time import sleep


def updater1(A):
    sleep(1)
    # for i in range(100):
    #     print("UPDATER 1:")


def updater2(A):
    sleep(1)
    # for i in range(100):
    #     print("UPDATER2:")


if __name__ == "__main__":
    pool = multiprocessing.Pool(4)
    start = time.time()
    # apply_async is better than map async for this purpose.
    pool.apply_async(updater1, [0])
    pool.apply_async(updater2, [0])
    pool.apply_async(updater1, [0])
    pool.apply_async(updater2, [0])
    pool.apply_async(updater1, [0])
    pool.apply_async(updater2, [0])
    pool.apply_async(updater1, [0])
    pool.apply_async(updater2, [0])
    pool.close()
    pool.join()
    stop = time.time()
    print("time ", stop - start)
