import schedule
from datetime import datetime

print('Введите сообщение')
s = input()
print('Введите период молачния (- для его отсутсвия)')
time_str = input()
time = None
if time_str != '-':
    time = map(int, time_str.split('-'))


def job():
    hour = datetime.now().time.hour
    if time[0] <= hour and hour <= time[1]:
        return
    hour = hour % 12
    if hour == 0:
        hour = 12
    print(s * hour)


schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
