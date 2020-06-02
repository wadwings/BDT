import json
import datetime
import re
import csv
import os

def load_json(filename):
    with os.open(filename, os.O_RDONLY) as f:
        t = json.load(f)
        data = {}
        data["city"] = t[0]["city"]
        for i in range(0, len(t)):
            del t[i]["city"]
            tmp = data[setTime(t[i]["time"])] = {}
            tmp["year"] = re.split('年|月|日', t[i]["time"])[0]
            tmp["month"] = re.split('年|月|日', t[i]["time"])[1]
            tmp["day"] = re.split('年|月|日', t[i]["time"])[2]
            tmp["w1"] = t[i]["weather"].split('/')[0]
            tmp["w2"] = t[i]["weather"].split('/')[1]
            tmp["tH"] = re.split('℃/|℃',t[i]["temperature"])[0]
            tmp["tL"] = re.split('℃/|℃',t[i]["temperature"])[1]
            tmp["wd1"] = wind(t[i]["wind"])[0]
            tmp["w1w"] = wind(t[i]["wind"])[1]
            tmp["w1s"] = wind(t[i]["wind"])[2]
            tmp["wd2"] = wind(t[i]["wind"])[3]
            tmp["w2w"] = wind(t[i]["wind"])[4]
            tmp["w2s"] = wind(t[i]["wind"])[5]
            print(tmp)
        return data
    return -1


def setTime(str):
    year = re.split('年|月|日', str)[0]
    month = re.split('年|月|日', str)[1]
    day = re.split('年|月|日', str)[2]
    return year + '.' + month + '.' + day + '.'


def wind(str):
    arr = [1,2,3,4,5,6]
    windData = re.split('风向|风/|-|级/|级|～|风|/', str)
    if windData[0] == "无持续":
        arr[0] = "none"
    else:
        arr[0] = windData[0]
    if windData[1] == "微":
        arr[1] = arr[2] = 0
    elif windData[1] == "≤3" or windData[1] == "<3" or windData[1] == "2":
        arr[1] = arr[2] = 2
    else:
        arr[1] = int(windData[1])
        arr[2] = int(windData[2])
    if windData[2].isdigit():
        if windData[3] == "无持续":
            arr[3] = "none"
        else:
            arr[3] = windData[3]
        if windData[4] == "微":
            arr[4] = arr[5] = 0
        elif windData[4] == "≤3" or windData[4] == "<3" or windData[4] == "2":
            arr[4] = arr[5] = 2
        else:
            arr[4] = int(windData[4])
            arr[5] = int(windData[5])
    else:
        if windData[2] == "无持续":
            arr[3] = "none"
        else:
            arr[3] = windData[2]
        if windData[3] == "微":
            arr[4] = arr[5] = 0
        elif windData[3] == "≤3" or windData[3] == "<3" or windData[3] == "2":
            arr[4] = arr[5] = 2
        else:
            arr[4] = int(windData[3])
            arr[5] = int(windData[4])
    return arr

load_json(os.path.join(os.path.dirname(os.path.abspath(__file__)),"sample/哈尔滨.json"))