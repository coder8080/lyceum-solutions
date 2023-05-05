import sys
import json

result = {'earlier': dict(), 'later': dict()}

divider = [17, 20]

for line in sys.stdin:
    line = line.strip('\n')
    time_str = line.split(': ')[0]
    text = ': '.join(line.split(': ')[1:])
    time = [int(el) for el in time_str.split('.')]
    if time < divider:
        result['earlier'][time_str] = text
    else:
        result['later'][time_str] = text

with open('report.json', 'w') as file:
    json.dump(result, file)
