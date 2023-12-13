import re

import pandas
import numpy as np
import pandas as pd
from Textdeal.exActor import divid_launch

screen_sum = divid_launch('../Joker.txt')

ul=[]
slug_info={}
i=0;index=0
for group in screen_sum:
    index=index+1
    door,time,place='','',''

    door = re.findall(r'(EXT|INT)', group[0])

    #提取 slugline 中的时间信息
    time1 = re.findall(r'(?<=- ).*(?=\W+)',group[0])
    time = re.findall(r'(?<=- ).*',time1[0])
    if len(time)>0:
        time_of_day = time[0].strip(' 0123456789')
    else:
        time_of_day= time1[0].strip(' 0123456789')

    if time_of_day =='CONTINUOUS':
        time_of_day=temp_time
    temp_time = time_of_day
    # print(index,time_of_day)
    #place
    place = re.findall(r'(?<=[EXT.|INT.]\s).*(?=[-])', group[0])
    slug_info['id']=index;slug_info['door']=door[0];slug_info['time']=time_of_day;slug_info['place']=place[0]

    if len(group)>1:
        i=i+1
        #get [NAME[dialgoe]],NAME[dialgoe],NAME[dialgoe],NAME[dialgoe]
        # for
        print(group)
    ul.append(slug_info)
    # print(li)


