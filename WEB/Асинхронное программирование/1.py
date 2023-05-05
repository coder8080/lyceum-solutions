
import time
import asyncio


async def task(name, make1, def1, make2, def2):
    await asyncio.sleep(make1 / 100)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(def1 / 100)
    print(f'{name} completed the 1 task.')
    await asyncio.sleep(make2 / 100)
    print(f'{name} moved on to the defense of the 2 task.')
    await asyncio.sleep(def2 / 100)
    print(f'{name} completed the 2 task.')


async def interviews_2(*pretendents):
    tasks = []
    for person in pretendents:
        name = person[0]
        print(f"{name} started the 1 task.")
    for person in pretendents:
        name = person[0]
        print(f"{name} started the 2 task.")
    for person in pretendents:
        tasks.append(task(*person))
    await asyncio.gather(*tasks)


data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews_2(*data))
print(time.time() - t0)
