import json
with open('data.json') as json_data:
    data = json.load(json_data)
    for key in data:
        for value in data[key]:
            print(key, ':', value)