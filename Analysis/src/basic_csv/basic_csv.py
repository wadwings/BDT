import csv
import datetime
import json
import os
import re
import pandas as pd

def load_json(filename):
    with open(filename, encoding = "utf-8") as f:
        t = json.load(f)
        data = {}
        if len(t):
            data["city"] = t[0]["city"].strip()
            for i in range(0, len(t)):
                del t[i]["city"]
                tmp = data[setTime(t[i]["time"])] = {}
                tmp["year"] = re.split('年|月|日', t[i]["time"])[0]
                tmp["month"] = re.split('年|月|日', t[i]["time"])[1]
                tmp["day"] = re.split('年|月|日', t[i]["time"])[2]
                tmp["w1"] = t[i]["weather"].split('/')[0]
                tmp["w2"] = t[i]["weather"].split('/')[1]
                tmp["tH"] = re.split('℃/|℃|/',t[i]["temperature"])[0]
                tmp["tL"] = re.split('℃/|℃|/',t[i]["temperature"])[1]
                tmp["wd1"] = wind(t[i]["wind"])[0]
                tmp["w1w"] = wind(t[i]["wind"])[1]
                tmp["w1s"] = wind(t[i]["wind"])[2]
                tmp["wd2"] = wind(t[i]["wind"])[3]
                tmp["w2w"] = wind(t[i]["wind"])[4]
                tmp["w2s"] = wind(t[i]["wind"])[5]
            pd.DataFrame(data).to_csv('{0}{1}.csv'.format(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../csv/'),data["city"]))
            return data


def setTime(str):
    year = re.split('年|月|日', str)[0]
    month = re.split('年|月|日', str)[1]
    day = re.split('年|月|日', str)[2]
    return year + '.' + month + '.' + day + '.'


def wind(str):
    arr = [1,2,3,4,5,6]
    windData = re.split('/', str)
    for i in range(0, 2):
        tmpData = re.split('风向|-|级|～|风', windData[i])
        if tmpData[0] == "无持续" or tmpData[0] == "" or tmpData[0] == "偏":
            arr[0 + i * 3] = "none"
        else:
            arr[0 + i * 3] = tmpData[0]
        if len(tmpData) > 1:
            if tmpData[1] == "≤3" or tmpData[1] == "<3" or tmpData[1] == "2":
                arr[1 + i * 3] = arr[2 + i * 3] = 2
            elif len(tmpData) > 2 and tmpData[1].isdigit() and tmpData[2].isdigit():
                arr[1 + i * 3] = int(tmpData[1])
                arr[2 + i * 3] = int(tmpData[2])
            else:
                arr[1 + i * 3] = arr[2 + i * 3]= 0
        else:
            arr[1 + i * 3] = arr[2 + i * 3]= 0
    return arr

#load_json(os.path.join(os.path.dirname(os.path.abspath(__file__)),"sample/哈尔滨.json"))
#load_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../Data/mapdata_basic/阿坝.json"))
