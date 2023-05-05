import asyncio


async def sowing(*plants):
    tasks = []
    for plant in plants:
        tasks.append(handle_plant(*plant))
    await asyncio.gather(*tasks)


async def handle_plant(*plant):
    name = plant[0]
    print(f'0 Beginning of sowing the {name} plant')
    tasks = [handle_plant_1(*plant), handle_plant_2(*plant),
             handle_plant_3(*plant)]
    await asyncio.gather(*tasks)
    print(f'9 The seedlings of the {name} are ready')


async def handle_plant_1(name, soaking, germination, survival):
    print(f'1 Soaking of the {name} started')
    await asyncio.sleep(soaking / 1000)
    print(f'2 Soaking of the {name} is finished')
    print(f'3 Shelter of the {name} is supplied')
    await asyncio.sleep(germination / 1000)
    print(f'4 Shelter of the {name} is removed')
    print(f'5 The {name} has been transplanted')
    await asyncio.sleep(survival / 1000)
    print(f'6 The {name} has taken root')


async def handle_plant_2(name, soaking, germination, survival):
    print(f'7 Application of fertilizers for {name}')
    await asyncio.sleep(3 / 1000)
    print(f'7 Fertilizers for the {name} have been introduced')


async def handle_plant_3(name, soaking, germination, survival):
    print(f'8 Treatment of {name} from pests')
    await asyncio.sleep(5 / 1000)
    print(f'8 The {name} is treated from pests')
