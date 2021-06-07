#coding:utf-8
import re
import json
from datetime import datetime
import pandas as pd
import requests



url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
page = requests.get(url).content.decode("utf-8")
regexp = "<script id=\"getAreaStat\">([^<]+)"

res = re.findall(regexp,page)
print(res)
'''
data = res[0][44:-11]
dicts = json.loads(data)

for row in dicts:
    for key in row:
        if key in ["creatTime","modifyTime"]:
            row[key] = datetime.fromisoformat(row[key]/1000).strftime("%Y-%m-%d %H:%M:%S")
        print(key,":",row[key],end=" ")

    print("\n")

df = pd.DateFrame(dicts)
df.to_csv("ncov1.csv",mode="a")
        
'''