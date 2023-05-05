import sqlite3
import csv


def convert_to_dict(i, elem):
    return {'no': i + 1, 'galaxy': elem[1], 'type': elem[2], 'size': elem[3], 'luminosity': elem[4], 'stars': elem[5]}


result_file = open('collisions.csv', 'w', encoding='utf-8')
writer = csv.DictWriter(
    result_file, fieldnames=['no', 'galaxy',
                             'type', 'luminosity', 'size', 'stars'],
    delimiter='#', quoting=csv.QUOTE_NONE)
writer.writeheader()

database_filename = input()
field_name = input()

# id, sign, type_id, size, luminosity_id, stars
ans = []

con = sqlite3.connect(database_filename)
cur = con.cursor()

min_value = -1
result = cur.execute(
    f'SELECT galaxies.id, {field_name} FROM galaxies INNER JOIN types ON' +
    ' galaxies.type_id = types.id INNER JOIN luminosities ON galaxies.lum' +
    'inosity_id = luminosities.id').fetchall()

min_ids = set()
min_value = -1

for elem in result:
    id = elem[0]
    value = elem[1]
    if min_value == -1 or value < min_value:
        min_value = value
        min_ids = {id}
    elif value == min_value:
        min_ids.add(id)

result = cur.execute(
    'SELECT galaxies.id, galaxies.sign, types.type, galaxies.size, lumi' +
    'nosities.range, galaxies.stars FROM galaxies INNER JOIN types ON galaxies.ty' +
    'pe_id = types.id INNER JOIN luminosities ON galaxies.luminosity_id' +
    f' = luminosities.id WHERE {field_name} = {min_value}')
ans = []
for elem in result:
    if elem[0] in min_ids:
        ans.append(elem)

ans.sort(key=lambda x: (x[3], x[1]), reverse=True)

for i, elem in enumerate(ans):
    writer.writerow(convert_to_dict(i, elem))

result_file.close()
