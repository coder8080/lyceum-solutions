import asyncio
from PIL import Image


def get_quarter_for_pixel(i, j, x, y):
    x_h = x // 2
    y_h = y // 2
    if i <= x_h and j <= y_h:
        return 2
    elif i <= x_h and j >= y_h:
        return 3
    elif i >= x_h and j <= y_h:
        return 1
    else:
        return 4


Q_MAP = ['', 'I', 'II', 'III', 'IV']


async def task(filename: str):
    print(f"Start {filename}")
    total_sum = 0
    im = Image.open(filename)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            total_sum += r + g + b
    await asyncio.sleep(0.1)
    total_count = x * y
    total_average = total_sum / total_count
    brightness_count = dict()
    amount = 0
    quarters = {1: 0, 2: 0, 3: 0, 4: 0}
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            pixel = pixels[i, j]
            current_sum = r + g + b
            if current_sum > total_average:
                amount += 1
                quarter = get_quarter_for_pixel(i, j, x, y)
                quarters[quarter] += 1
                if pixel not in brightness_count:
                    brightness_count[pixel] = 0
                brightness_count[pixel] += 1
    items = list(brightness_count.items())
    items.sort(key=lambda x: x[1], reverse=True)
    most_often_item = items[0]
    most_often_count = most_often_item[1]
    percent = int(most_often_count * 100_000 / total_count)
    amount = int(amount * 100 / total_count)

    quarter_items = list(quarters.items())
    quarter_items.sort(key=lambda x: x[1], reverse=True)
    top_quarter = Q_MAP[quarter_items[0][0]]

    print(f'Done {filename}, percent {percent}')
    print(f'Done {filename}, amount {amount}')
    print(f'Done {filename}, quarter {top_quarter}')
    print(f'Ready {filename}')

    return (filename, percent, amount, top_quarter)


async def asteroids(*filenames):
    tasks = []
    for filename in filenames:
        tasks.append(task(filename))
    result = await asyncio.gather(*tasks)
    return result

data = ['1.jpg']
print(asyncio.run(asteroids(*data)))
