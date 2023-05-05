import argparse
import requests
import csv

parser = argparse.ArgumentParser(description="no deskription")
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)
parser.add_argument('--multiply', type=int, default=5)
parser.add_argument('--larger', type=int, default=0)

args = parser.parse_args()

host = args.host
port = args.port
multiply = args.multiply
minimum = args.larger

url = f"http://{host}:{port}"

data = requests.get(url).json()

result_file = open('anomalies.csv', 'w')
writer = csv.writer(result_file, delimiter=',')

ans = list()

for key, values in data.items():
    row = [key]
    values = list(filter(lambda x: x >= minimum and x % multiply != 0, values))
    positive_minimum = -1
    for item in values:
        if item > 0 and item % multiply != 0:
            if positive_minimum == -1 or item < positive_minimum:
                positive_minimum = item
    row.append(positive_minimum)
    maximum = max(values)
    row.append(maximum)
    second_sum = 0
    for item in values[0::2]:
        second_sum += item
    row.append(second_sum)
    second_sum = 0
    for item in values[1::2]:
        second_sum += item
    row.append(second_sum)
    ans.append(row)

ans.sort()
for row in ans:
    writer.writerow(row)

result_file.close()
