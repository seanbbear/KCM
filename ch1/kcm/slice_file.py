import json
import jieba
import jieba.posseg
import re

import time
start=time.time()
######
# import heapq
li=[]
li_sliced=[]
seg=[]
seg_s=[]
limit=50000
file_count=0
# path='C:/Users/udic/Desktop/prac/sliced_file/'
path='C:/Users/k7489/OneDrive/桌面/sean/prac/sliced_file/'
with open('wiki20180805_fullText.json','r',encoding='utf-8') as file:
    for line in file:
        li=re.split('，|。',line.strip())
        for i in range(len(li)):
            li[i]=re.sub("[\\s+\\.\\!\\/_,$%^*(+\"\']+|[+——！？：:、·-“\\\《》；~@#￥%……&*{（）}()”「」／]+".encode('utf-8').decode('utf-8'), "".encode('utf-8').decode('utf-8'),li[i])
            sente=''.join(li[i]).replace('\\n','')
            sente=sente.replace(' ','')   
            seg.append(jieba.lcut(sente))
        if len(seg)<limit:
            continue
        with open(path+'file'+str(file_count)+'.json','w',encoding='utf-8') as file:
            json.dump(seg,file,ensure_ascii=False)
            seg=[]
            end=time.time()
            print(str(end-start)+'秒')
            file_count+=1
with open(path+'file'+str(file_count)+'.json','w',encoding='utf-8') as file:
        json.dump(seg,file,ensure_ascii=False)
 



    
