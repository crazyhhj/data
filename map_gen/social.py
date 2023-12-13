import infomap
import json
with open('../data/freRealtion', 'r') as f:
    information = json.load(f)

person_list = {}
actor_relation = []

tmp = {}
for i in information:
    for j in i:
        a = list(j.values())
        actor_unit = set(a[:2])
        if(tmp == actor_unit):
            continue
        if len(actor_unit)==1:
            continue
        tmp = actor_unit
        actor_relation.append(j)

# for i in actor_relation:
#     print(i.values())
#     print(i)


for i in actor_relation:
        person_list[i['source']] = 0
        person_list[i['target']] = 0

index = 0
for i,j in person_list.items():
    person_list[i] = index
    index = index + 1

#
#
#
person_set = list(person_list)
print(len(actor_relation))
infomapWrapper = infomap.Infomap(flow_model="undirected")
for i in actor_relation:
    infomapWrapper.addLink(person_list[i['source']], person_list[i['target']], i['value'])
#
# 运行 Infomap 算法
infomapWrapper.run()

res = []
# 输出结果
for node in infomapWrapper.iterTree():
    # print(node.moduleIndex())
    if node.isLeaf():
        res.append({"Node": person_set[node.physicalId], "Community": node.moduleIndex()})
        print("Node:", node.physicalId, "Community:", node.moduleIndex())

jstring = json.dumps(res)
jsFile = open('../data/actor_group.json', 'w')
jsFile.write(jstring)
jsFile.close()
print(res)
