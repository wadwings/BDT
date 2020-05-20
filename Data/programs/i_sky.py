import io,os,requests,json,copy
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

keys=['city','time','max','min','a_max','a_min','sunny','rainy','cloudy','snowy']
infor_temp={}.fromkeys(keys)

ua=UserAgent()

for i in [3837,3842,3850,3856,3870,3874,3880,3889,3905,3909,3914,3916,3937,3942,3944,3946,3949,3965,3969,3971]:
    url='http://tianqihoubao.com/guoji/{}.html'.format(str(i))
    headers={'User-Agent':ua.random}
    
    trytimes=0
    while(trytimes<20):
        try:
            res=requests.get(url,headers=headers,timeout=3)
            if res.status_code==200:
                break
        except:
            trytimes+=1
            print('序号{} 请求失败第{}次'.format(str(i),trytimes+1))
    if trytimes==20:
        continue

    soup=BeautifulSoup(res.text,'html.parser')
    city=soup.select('#content > h1')
    city=city[0].string
    city=city[:city.find('历')]

    infor=[]
    data={}
    data[0]=soup.select('#bd > div.hd > table > tr > td:nth-child(1) > a')
    for number in range(1,9):
        data[number]=soup.select('#bd > div.hd > table > tr > td:nth-child({}) > span'.format(str(number+1)))
    infor_temp['city']=city
    count=0
    while(count<len(data[0])):
        temp=copy.deepcopy(infor_temp)
        for number in range(9):
            t=data[number][count].string
            t=t.string.replace('\n','').replace('\r','').replace(' ','')
            temp[keys[number+1]]=t     
        infor.append(temp)
        count+=1
    
    json_data=json.dumps(infor,indent=4,ensure_ascii=False)
    with io.open('../mapdata_i/{}.json'.format(city),'w',encoding='utf-8') as fp:
        fp.write(json_data)
    print(city)

for it in range(3976,4269):
    url='http://tianqihoubao.com/guoji/{}.html'.format(str(it))
    headers={'User-Agent':ua.random}
    
    trytimes=0
    while(trytimes<20):
        try:
            res=requests.get(url,headers=headers,timeout=3)
            if res.status_code==200:
                break
        except:
            trytimes+=1
            print('序号{} 请求失败第{}次'.format(str(i),trytimes+1))
    if trytimes==20:
        continue

    soup=BeautifulSoup(res.text,'html.parser')
    city=soup.select('#content > h1')
    city=city[0].string
    city=city[:city.find('历')]

    infor=[]
    data={}
    data[0]=soup.select('#bd > div.hd > table > tr > td:nth-child(1) > a')
    for number in range(1,9):
        data[number]=soup.select('#bd > div.hd > table > tr > td:nth-child({}) > span'.format(str(number+1)))
    infor_temp['city']=city
    count=0
    while(count<len(data[0])):
        temp=copy.deepcopy(infor_temp)
        for number in range(9):
            t=data[number][count].string
            t=t.string.replace('\n','').replace('\r','').replace(' ','')
            temp[keys[number+1]]=t     
        infor.append(temp)
        count+=1
    
    json_data=json.dumps(infor,indent=4,ensure_ascii=False)
    with io.open('../mapdata_i/{}.json'.format(city),'w',encoding='utf-8') as fp:
        fp.write(json_data)
    print(city)
