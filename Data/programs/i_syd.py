import requests       #导入requests包
from bs4 import    BeautifulSoup
from fake_useragent import UserAgent
import json
import io
import time
import random


def requestDemo(url,headers):
    trytimes = 20  #  重试的次数
    for i in range(trytimes):
        try:
            proxies = None
            response = requests.get(url, headers=headers, verify=False, proxies=None, timeout=2)
            #	注意此处也可能是302等状态码
            if response.status_code == 200:
                return response
        except:
        # logdebug(f'requests failed {i}time')
            f = open('fault.2','a',encoding='utf-8')
            f.write(f'{url} requests failed {i+1} time')
            f.write('\n')
            f.close()



number = 1

while (number < 2135):
    infor = []
    count = 0
    url = 'http://www.tianqihoubao.com/guoji/{}.html'.format(number)
    ua = UserAgent()
    headers={"User-Agent":ua.random}
    strhtml =requestDemo(url,headers)

    if strhtml != None:#网页正常访问
                strhtml.encoding = 'gbk'
                soup=BeautifulSoup(strhtml.content,'lxml')
                if strhtml.encoding != None:
                 p=soup.h1.string
                 x = len(p)
                 y = x - 9
                 p2 = p[0:y]
                 commid2=soup.find_all('div',class_='hd')
                 for info in commid2:
                     tr_list = info.find_all('tr')[1:]       # 使用切片取到第2个tr标签
                     for index, tr in enumerate(tr_list):     # enumerate可以返回元素的位置及内容
                        td_list = tr.find_all('td')
                        time = td_list[0].text
                        time = ''.join(time.split())
                        max = td_list[1].text
                        max = ''.join(max.split())
                        min = td_list[2].text
                        min = ''.join(min.split())
                        a_max = td_list[3].text
                        a_max = ''.join(a_max.split())
                        a_min = td_list[4].text
                        a_min= ''.join(a_min.split())
                        sunny = td_list[5].text
                        sunny = ''.join(sunny.split())
                        rainy = td_list[6].text
                        rainy = ''.join(rainy.split())
                        cloudy = td_list[7].text
                        cloudy = ''.join(cloudy.split())
                        snowy = td_list[8].text
                        snowy = ''.join(snowy.split())
                        infor.append({'city': p2})
                        infor[count]['time'] =time
                        infor[count]['max'] =max
                        infor[count]['min'] = min
                        infor[count]['a_max'] = a_max
                        infor[count]['a_min'] = a_min
                        infor[count]['sunny'] = sunny
                        infor[count]['rainy'] = rainy
                        infor[count]['cloudy'] = cloudy
                        infor[count]['snowy'] = snowy
                        count = count+1
                        print(infor)
                        json_data = json.dumps(infor, indent=4, ensure_ascii=False)
                        with io.open('../mapdata_i/{}.json'.format(p2), 'w', encoding='utf-8') as fp:
                            fp.write(json_data)
                number += 1
                print(number)


    else: number = number+1
    continue
