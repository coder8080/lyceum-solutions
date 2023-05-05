from flask import Flask, jsonify
import sqlite3
from functools import cmp_to_key

app = Flask(__name__)

data_file = open('carbon.txt', encoding='utf-8')
database_filename = data_file.readline().strip('\n')
max_temp = int(data_file.readline().strip('\n'))
data_file.close()


def compare(item1, item2):
    if item1['temperature'] < item2['temperature']:
        return -1
    elif item1['temperature'] == item2['temperature']:
        if item1['mass'] > item2['mass']:
            return -1
        elif item1['mass'] == item2['mass']:
            return 0
        elif item1['mass'] < item2['mass']:
            return 1
    elif item1['temperature'] > item2['temperature']:
        return 1


def convert_to_dict(item):
    return {'star': item[0], 'temperature': item[1], 'mass': item[2], 'size': item[3]}


@app.route('/darkness', methods=['GET'])
def darkness():
    con = sqlite3.connect(database_filename)
    cur = con.cursor()
    result = cur.execute(
        'SELECT star, temperature, mass, size ' +
        f'FROM stars WHERE stage = "C" AND temperature <= {max_temp}').fetchall()
    result = [convert_to_dict(el) for el in result]
    result = sorted(result, key=cmp_to_key(compare))
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
