import asyncio
import time
from rich import print


async def todo_task(task_name: str, delay: float = 1.0) -> dict:
    print(f"Starting {task_name}")
    await asyncio.sleep(delay=delay)
    print(f"Completed {task_name}")
    return { "task" : task_name, "status" : "completed"}

async def main():
    start = time.perf_counter()
    todo = ['get package', 'laundry', 'bake cake']

    #for item in todo:
        #await todo_task(item)

    # Type 1
    # tasks_list = [asyncio.create_task(todo_task(task_name=item)) for item in todo]
    # done, pending = await asyncio.wait(tasks_list)

    # Type 2
    coros = [todo_task(item) for item in todo]
    results = await asyncio.gather(*coros, return_exceptions=True)

    end = time.perf_counter()
    #print(*[res.result() for res in done])
    print(results)
    #print(pending)
    print(f"Execution time is {end-start:.2f}s")

if __name__ == '__main__':
    asyncio.run(main())
