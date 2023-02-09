import json

file = open('scoring.json', mode='rt', encoding='utf-8')
data = json.load(file)
file.close()
del file
score_for_test = dict()
test_count = 0
for entry in data['scoring']:
    tests = entry['required_tests']
    total_points = entry['points']
    points_for_test = int(total_points / len(tests))
    for test in tests:
        score_for_test[test] = points_for_test
    test_count += len(tests)
ans = 0
for i in range(1, test_count + 1):
    status = input()
    if status == 'ok':
        ans += score_for_test[i]
print(ans)
