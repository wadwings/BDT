import requests       #导入requests包
from bs4 import    BeautifulSoup
from fake_useragent import UserAgent
import json
import io
import time
import random
target_year_list = ["2011", "2012", "2013", "2014", "2015","2016","2017","2018","2019"]
target_month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

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
            f = open('fault','a',encoding='utf-8')
            f.write(f'{url} requests failed {i+1} time')
            f.write('\n')
            f.close()

#def get_urls(city_pinyin):
#    urls = []
#    for i in city_pinyin.keys():
#      for year in target_year_list:
#         for month in target_month_list:
#             date = year + month
#             urls.append('http://www.tianqihoubao.com/lishi/'+i+'/month/{}.html'.format(date))

#     return urls
city = {    
    "beijing": "北京",
    "tianjin": "天津",
    "shijiazhuang": "石家庄",
    "tangshan": "唐山",
    "qinhuangdao": "秦皇岛",
    "handan": "邯郸",
    "xingtai": "邢台",
    "baoding": "保定",
    "zhangjiakou": "张家口",
    "chengde": "承德",
    "cangzhou": "沧州",
    "langfang": "廊坊",
    "hengshui": "衡水",
    "taiyuan": "太原",
    "datong": "大同",
    "yangquan": "阳泉",
    "changzhi": "长治",
    "jincheng": "晋城",
    "shuozhou": "朔州",
    "jinzhong": "晋中",
    "sxyuncheng": "运城",
    "xinzhou": "忻州",
    "linfen": "临汾",
    "lvliang": "吕梁",
    "huhehaote": "呼和浩特",
    "baotou": "包头",
    "wuhai": "乌海",
    "chifeng": "赤峰",
    "tongliao": "通辽",
    "eerduosi": "鄂尔多斯",
    "hulunbeier": "呼伦贝尔",
    "bayannaoer": "巴彦淖尔",
    "wulanchabu": "乌兰察布",
    "xinganmeng": "兴安盟",
    "xilinguole": "锡林郭勒",
    "alashanmeng": "阿拉善盟",
    "shenyang": "沈阳",
    "dalian": "大连",
    "anshan": "鞍山",
    "fushun": "抚顺",
    "benxi": "本溪",
    "dandong": "丹东",
    "jinzhou": "锦州",
    "yingkou": "营口",
    "fuxin": "阜新",
    "liaoyang": "辽阳",
    "panjin": "盘锦",
    "changtu": "昌图",
    "chaoyang": "朝阳",
    "huludao": "葫芦岛",
    "changchun": "长春",
    "jilin": "吉林",
    "siping": "四平",
    "liaoyuan": "辽源",
    "tonghua": "通化",
    "baishan": "白山",
    "songyuan": "松原",
    "baicheng": "白城",
    "yanbian": "延边",
    "haerbin": "哈尔滨",
    "qiqihaer": "齐齐哈尔",
    "jixi": "鸡西",
    "hegang": "鹤岗",
    "shuangyashan": "双鸭山",
    "daqing": "大庆",
    "yichun": "伊春",
    "jiamusi": "佳木斯",
    "qitaihe": "七台河",
    "mudanjiang": "牡丹江",
    "heihe": "黑河",
    "suihua": "绥化",
    "daxinganling": "大兴安岭",
    "shanghai": "上海",
    "nanjing": "南京",
    "wuxi": "无锡",
    "xuzhou": "徐州",
    "changzhou": "常州",
    "suzhou": "苏州",
    "nantong": "南通",
    "lianyungang": "连云港",
    "huaian": "淮安",
    "yancheng": "盐城",
    "yangzhou": "扬州",
    "zhenjiang": "镇江",
    "jstaizhou": "泰州",
    "suqian": "宿迁",
    "hangzhou": "杭州",
    "ningbo": "宁波",
    "wenzhou": "温州",
    "jiaxing": "嘉兴",
    "huzhou": "湖州",
    "shaoxing": "绍兴",
    "jinhua": "金华",
    "quzhou": "衢州",
    "zhoushan": "舟山",
    "taizhou": "台州",
    "lishui": "丽水",
    "hefei": "合肥",
    "wuhu": "芜湖",
    "bangbu": "蚌埠",
    "huainan": "淮南",
    "maanshan": "马鞍山",
    "huaibei": "淮北",
    "tongling": "铜陵",
    "anqing": "安庆",
    "huangshan": "黄山",
    "chuzhou": "滁州",
    "fuyang": "阜阳",
    "anhuisuzhou": "宿州",
    "chaohu": "巢湖",
    "liuan": "六安",
    "bozhou": "亳州",
    "chizhou": "池州",
    "xuancheng": "宣城",
    "fujianfuzhou": "福州",
    "xiamen": "厦门",
    "putian": "莆田",
    "sanming": "三明",
    "quanzhou": "泉州",
    "zhangzhou": "漳州",
    "nanping": "南平",
    "longyan": "龙岩",
    "ningde": "宁德",
    "nanchang": "南昌",
    "jingdezhen": "景德镇",
    "pingxiang": "萍乡",
    "jiujiang": "九江",
    "xinyu": "新余",
    "yingtan": "鹰潭",
    "ganzhou": "赣州",
    "jian": "吉安",
    "jxyichun": "宜春",
    "fuzhou": "抚州",
    "shangrao": "上饶",
    "jinan": "济南",
    "qingdao": "青岛",
    "zibo": "淄博",
    "zaozhuang": "枣庄",
    "dongying": "东营",
    "yantai": "烟台",
    "weifang": "潍坊",
    "sdjining": "济宁",
    "taian": "泰安",
    "weihai": "威海",
    "rizhao": "日照",
    "laiwu": "莱芜",
    "linyi": "临沂",
    "dezhou": "德州",
    "liaocheng": "聊城",
    "binzhou": "滨州",
    "heze": "菏泽",
    "zhengzhou": "郑州",
    "kaifeng": "开封",
    "lvyang": "洛阳",
    "pingdingshan": "平顶山",
    "anyang": "安阳",
    "hebi": "鹤壁",
    "xinxiang": "新乡",
    "jiaozuo": "焦作",
    "puyang": "濮阳",
    "xuchang": "许昌",
    "luohe": "漯河",
    "sanmenxia": "三门峡",
    "nanyang": "南阳",
    "shangqiu": "商丘",
    "xinyang": "信阳",
    "zhoukou": "周口",
    "zhumadian": "驻马店"
    }





for i in city.keys():
    infor = []
    count = 0
    for year in target_year_list:
        for month in target_month_list:
            date = year + month
            url = 'http://www.tianqihoubao.com/lishi/' + i + '/month/{}.html'.format(date)
            ua = UserAgent()
            headers={"User-Agent":ua.random}
            strhtml =requestDemo(url,headers)
            strhtml.encoding = 'gbk'
            if strhtml.status_code == 200:#网页正常访问
                soup=BeautifulSoup(strhtml.content,'lxml')
                commid2=soup.find_all('div',class_='wdetail')
                for info in commid2:
                  tr_list = info.find_all('tr')[1:]       # 使用切片取到第2个tr标签
                  for index, tr in enumerate(tr_list):     # enumerate可以返回元素的位置及内容
                        td_list = tr.find_all('td')
                        time = td_list[0].text
                        time = ''.join(time.split())
                        weather = td_list[1].text
                        weather = ''.join(weather.split())
                        temperature = td_list[2].text
                        temperature = ''.join(temperature.split())
                        wind = td_list[3].text
                        wind = ''.join(wind.split())
                        infor.append({'city': city[i]})
                        infor[count]['time'] =time
                        infor[count]['weather'] = weather
                        infor[count]['temperature'] = temperature
                        infor[count]['wind'] = wind
                        count = count+1
                        print(infor)
#                  else:continue
    json_data = json.dumps(infor, indent=4, ensure_ascii=False)
    with io.open('../mapdata_basic/{}.json'.format(city[i]), 'w', encoding='utf-8') as fp:
        fp.write(json_data)