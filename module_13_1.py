import asyncio

async def start_strogman(name, power):
    print(f'Силач {name} начал соревнавания.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнавания.')


async def start_tuornament():
    task1 = asyncio.create_task(start_strogman('Паша', 3))
    task2 = asyncio.create_task(start_strogman('Денис', 4))
    task3 = asyncio.create_task(start_strogman('Апполон', 5))

    await task1
    await task2
    await task3

asyncio.run(start_tuornament())