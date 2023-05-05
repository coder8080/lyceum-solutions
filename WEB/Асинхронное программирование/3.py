import sys
import time
import asyncio


div = 100


async def handle_gift(gift):
    print(f'Buy {gift["name"]}')
    time.sleep(gift['choose'] / div)
    await asyncio.sleep(gift['buy'] / div)
    print(f"Got {gift['name']}")


async def main():
    stops = []
    gifts = []
    # получаем все остановки
    for line in sys.stdin:
        line = line.strip('\n')
        if line == '':
            break
        time, _ = [int(el) for el in line.split()]
        stops.append(time)

    # получаем все подарки
    for line in sys.stdin:
        line = line.strip('\n')
        if len(line) == 0:
            continue
        name, choose, buy = line.split()
        choose = int(choose)
        buy = int(buy)
        gifts.append({'name': name, 'choose': choose,
                      'buy': buy, 'total': choose + buy})

    # сортируем подарки от самого долгого к самому котороткому
    gifts.sort(key=lambda x: (x['total'], x['choose']), reverse=True)

    # едем по остановкам
    for i, s in enumerate(stops):
        print(f'Buying gifts at {i + 1} stop')
        time_left = s
        gifts_to_buy = []
        for gift in gifts:
            total = gift['total']
            # total должен вмещаться в оставшееся время
            if total <= time_left:
                # вычитаем только выбор, упаковка ассинхронная
                time_left -= gift['choose']
                gifts_to_buy.append(gift)
        tasks = []
        for gift in gifts_to_buy:
            tasks.append(handle_gift(gift))
        await asyncio.gather(*tasks)
        gifts = list(filter(lambda x: x not in gifts_to_buy, gifts))
        print(f'Arrive from {i + 1} stop')
    if len(gifts) > 0:
        print('Buying gifts after arrival')
        tasks = []
        for gift in gifts:
            tasks.append(handle_gift(gift))
        await asyncio.gather(*tasks)


asyncio.run(main())
