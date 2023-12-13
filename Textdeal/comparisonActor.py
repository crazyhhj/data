import json

with open('../data/film_event_data.json', 'r') as f:
    information = json.load(f)

with open('../data/gpt_result_slim_f.json', 'r') as t:
    type_info = json.load(t)

print(len(information), len(type_info))

index = 0
for i in information:
    for j in i:
        try:
            print(j['Person'],j['Behavior'])
        except:
            print(j)

