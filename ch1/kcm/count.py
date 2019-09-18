import json
import os
from collections import Counter 
import sys


path = 'C:/Users/k7489/OneDrive/桌面/sean/碩0暑假/Data/sliced_file_ch1/'
num_files=0
path_list = os.listdir(path)
path_list.sort()

seg=[]
seg_used=[]
keyword = input("請輸入keyword:")
for filename in path_list:
    print(os.path.join(path,filename))
    with open(os.path.join(path,filename),'r',encoding='utf-8') as file:
        seg=json.load(file)
        for i in range(len(seg)):
                if keyword in seg[i]:
                        seg_used=seg_used+seg[i]
        counted=Counter(seg_used).most_common(11)

list(counted)
counted.pop(0)
print(counted)






