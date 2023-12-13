import re
import json
from copy import deepcopy


#得到场景 screenplay的片段名
def screenplay(film_script_txtfile_path):
    slug_lines = r'(EXT\..*|INT\..*)'
    # slug_lines = "EXT.*|INT.*"
    # slug_lines = ".*(?=:\n"
    with open(film_script_txtfile_path, "r",encoding='utf-8') as f:
        film_string = f.readlines()
    senceplay=[]
    for line in film_string:

        valid = re.findall(slug_lines,line)
        if valid:
            # print(line)
            print(valid[0])
            senceplay.append(valid[0])
    return senceplay

#提取 slug lines 中信息的函数 并打包成列表【INT/ENT】【PLEACE】【TIMEING】
# 提取 电影 转场(TRANSITIONS) 词段  并且 提取转场到哪一幕
def transitions_ex(film_script_txtfile_path):
    transitions = r'.*(?=:\n)'
    # slug_lines = "^\d+.*[EXT|INT].*"
    slug_lines = "(EXT\..*|INT\..*)"
    #get file list
    with open(film_script_txtfile_path, "r", encoding='utf-8') as f:
        film_string = f.readlines()
    transitions_list = []
    info_tran = []
    i = 0
    j = 0
    for line in film_string:
        temp = []
        tran_span = re.findall(transitions,line)
        #get [CUT TO][FADE IN] like this
        if tran_span:
            print(tran_span)
            transitions_list.append(tran_span)
            temp.append(tran_span)
            #当找到 转场词 开始搜寻接下来的 动作 直到 找到下一个slug line
            j = i+1
            while len(film_string)-j:
                if(film_string[j]!='\n'):
                    temp.append(film_string[j])
                    v = re.findall(slug_lines, film_string[j])
                    if v:
                        break
                j=j+1
            info_tran.append(temp)
        i = i + 1
    print(transitions_list, info_tran)
    return transitions_list, info_tran

transitions_ex('Halloween.txt')