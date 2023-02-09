import schedule
from datetime import datetime


def job():
    hour = datetime.now().time.hour % 12
    if hour == 0:
        hour = 12
    print('Ку' * hour)


schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
