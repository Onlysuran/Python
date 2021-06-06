#coding:utf-8
from aip import AipSpeech
import json

APP_ID = '24320412'
API_KEY = 'EwBjm2jXQdnyNW6ZdzORLxTc'
SECRET_KEY = 'PKnlVQmc2gl6mf0c3dWVaKYsGTFyGj7N'

clinet = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

s = '我是苏然'
speak = clinet.synthesis(s,'zh',1,{
    'vol': 5,   #音量，取值0-15，默认为5中音量
    'per': 3,   
    'spd': 6,   #语速，取值0-9，默认为5中语速
    'pit': 3 ,  #音调，取值0-9，默认为5中语调
})

with open('myspeek.mp3','w') as f: 
    f.write(speak)
    