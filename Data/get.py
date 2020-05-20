import json,os,io

with io.open('./index_i.json','r',encoding='utf-8') as fp:
    infor=json.load(fp)
for continent in infor