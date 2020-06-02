import io,os,requests,json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua=UserAgent()
headers={'User-Agent':ua.random}
url1='http://tianqihoubao.com/guoji/'
headers={'User-Agent':ua.random}
try:
    res=requests.get(url1,headers=headers,timeout=10)
    res.encoding='gbk'
except:
    os._exit(0)
soup=BeautifulSoup(res.text,'html.parser')
keys=['亚洲','欧洲','美洲','非洲','大洋洲']
infor={}
for i in range(5):
    infor[keys[i]]={}
    data1=soup.select('#content > div.citychk > dl:nth-child({}) > dd > a'.format(str(i+1)))
    for country in data1:
        url2=country.get('href')
        country=country.string
        infor[keys[i]][country]={}
        try:
            res2=requests.get('http://tianqihoubao.com'+url2,headers=headers,timeout=10)
            res2.encoding='utf-8'
        except:
            os._exit(0)
        soup2=BeautifulSoup(res2.text,'html.parser')
        data2=soup2.select('#content > div.citychk > dl > dd > a')
        for city in data2:
            city=city.string
            infor[keys[i]][country][city]={
                'name':city,
                'path':'/mapdata_i/{}.json'.format(city)
            }
json_data=json.dumps(infor,indent=4,ensure_ascii=False)
with io.open('../index_i.json','w',encoding='utf-8') as fp:
    fp.write(json_data)
        
