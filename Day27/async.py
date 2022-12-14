# cfe.sh/github -> 30 Day of Python -> Day 27
import time
import asyncio

iteration_times = [1, 3, 2, 4]


async def sleeper(seconds, i=-1):
    start_time = time.time()
    if i != -1:
        print(f"{i}\t{seconds}s")
    await asyncio.sleep(seconds)
    return time.time() - start_time


run_time = 0
total_compute_run_time = 0


async def main1():  # coroutine object
    global run_time
    global total_compute_run_time

    # await sleeper(1, i=0)       #čakaj, kým dokončí volaná funa
    tasks = []

    for i, second in enumerate(iteration_times):
        result = await sleeper(second, i=i)
        run_time += result


async def main():  # coroutine object
    global run_time
    global total_compute_run_time

    # await sleeper(1, i=0)       #čakaj, kým dokončí volaná funa
    tasks = []

    for i, second in enumerate(iteration_times):    #tu sa zostaví task list
        tasks.append(
            asyncio.create_task(
                sleeper(second, i=i)
            )
        )
    results = await asyncio.gather(*tasks) #gather execute task list
    print(results)
    for run_time_result in results:
        total_compute_run_time += run_time_result
        if run_time_result > run_time:
            run_time += run_time_result


# main()
asyncio.run(main())
print(f"Ran for {run_time} seconds")

print(f"Ran for {run_time} seconds, with a total of {total_compute_run_time} and {run_time / total_compute_run_time}")
