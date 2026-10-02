# parallelism consists of executing multiple operations at the same time

# multiprocessing is a means of achieving parallelism that entails spreading tasks over computer's
# central processing unit (CPU) cores. Multiprocessing is well-suited for CPU-bound tasks, such as
# tightly bound for loops and mathematcal computations

# concurrency is a slightly broader term than parallelism, suggesting that multiple tasks
# have the ability to run in an overlapping manner. Concurrency doesn't necessarily imply parallelism

# threading is a concurrent execution model in which multiple threads take turns executing tasks. 
# A single process can contain multiple threads


import asyncio
async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    