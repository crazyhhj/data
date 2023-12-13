import json

with open('../data/gpt_result_slim.json') as f:
    gpt = json.load(f)

with open('../data/clear_text.json') as f:
    clear = json.load(f)
    clear = clear[1:]
idx = 0
ad =0
while(idx < len(gpt)):
    ap = 0
    for i in gpt[idx]:
        gpt[idx][ap]['sentence'] = clear[idx][ap]
        ap = ap + 1
    idx = idx + 1

jstring = json.dumps(gpt)
jsonFile = open("../data/gpt_result_slim_f.json", "w")
jsonFile.write(jstring)
jsonFile.close()