import json
import time

def load_tem(filename):
    f = open(filename, encoding='utf-8');
    t = json.load(f)
    for i in t:
        i["time"] = time.mktime(time.strptime(i["time"],"%Y年%m月%d日"))
        i["weather"] = i["weather"].split("/")
        i["temperature"] = i["temperature"].split("/")

