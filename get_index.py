import requests,io,json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua=UserAgent()
url='http://tianqihoubao.com/lishi/'
headers={'User-Agent':ua.random}
res=requests.get(url=url,headers=headers)
res.encoding='gbk'
soup=BeautifulSoup(res.text,'html.parser')
infor={}
for i in range(34):
    province=soup.select('#content > div.citychk > dl:nth-child({}) > dt >a'.format(str(i+1)))
    cities=soup.select('#content > div.citychk > dl:nth-child({}) > dd > a'.format(str(i+1)))
    province=province[0].string.replace(' ','')
    infor[province]={}
    for city in cities:
        city=city.string.replace(' ','')
        infor[province][city]={
            'name':city,
            'path':'/mapdata/{}.json'.format(city)
        }

json_data=json.dumps(infor,indent=4,ensure_ascii=False)
with io.open('./index.json','w',encoding='utf-8') as fp:
    fp.write(json_data)
