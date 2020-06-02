import io
import os
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

city={
    "wuhan": "武汉",
    "huangshi": "黄石",
    "shiyan": "十堰",
    "yichang": "宜昌",
    "xiangyang": "襄阳",
    "ezhou": "鄂州",
    "jingmen": "荆门",
    "xiaogan": "孝感",
    "jingzhou": "荆州",
    "huanggang": "黄冈",
    "xianning": "咸宁",
    "suizhou": "随州",
    "enshi": "恩施",
    "xiantao": "仙桃",
    "qianjiang": "潜江",
    "tianmen": "天门",
    "shennongjia": "神农架",
    "changsha": "长沙",
    "zhuzhou": "株洲",
    "xiangtan": "湘潭",
    "hengyang": "衡阳",
    "shaoyang": "邵阳",
    "yueyang": "岳阳",
    "changde": "常德",
    "zhangjiajie": "张家界",
    "yiyang": "益阳",
    "chenzhou": "郴州",
    "yongzhou": "永州",
    "huaihua": "怀化",
    "loudi": "娄底",
    "xiangxi": "湘西",
    "guangzhou": "广州",
    "shaoguan": "韶关",
    "shenzhen": "深圳",
    "zhuhai": "珠海",
    "shantou": "汕头",
    "foshan": "佛山",
    "jiangmen": "江门",
    "zhanjiang": "湛江",
    "maoming": "茂名",
    "zhaoqing": "肇庆",
    "huizhou": "惠州",
    "meizhou": "梅州",
    "shanwei": "汕尾",
    "heyuan": "河源",
    "yangjiang": "阳江",
    "gdqingyuan": "清远",
    "dongguang": "东莞",
    "zhongshan": "中山",
    "chaozhou": "潮州",
    "jieyang": "揭阳",
    "yunfu": "云浮",
    "nanning": "南宁",
    "liuzhou": "柳州",
    "guilin": "桂林",
    "wuzhou": "梧州",
    "beihai": "北海",
    "fangchenggang": "防城港",
    "gxqinzhou": "钦州",
    "guigang": "贵港",
    "guangxiyulin": "玉林",
    "baise": "百色",
    "hezhou": "贺州",
    "hechi": "河池",
    "laibin": "来宾",
    "chongzuo": "崇左",
    "haikou": "海口",
    "sanya": "三亚",
    "wuzhishan": "五指山",
    "qionghai": "琼海",
    "danzhou": "儋州",
    "wenchang": "文昌",
    "wanning": "万宁",
    "dongfang": "东方",
    "dingan": "定安",
    "tunchang": "屯昌",
    "chengmai": "澄迈",
    "lingao": "临高",
    "baisha": "白沙",
    "changjiang": "昌江",
    "lingshui": "陵水",
    "xishaqundao": "西沙群岛",
    "nanshaqundao": "南沙群岛",
    "chongqing": "重庆",
    "chengdu": "成都",
    "zigong": "自贡",
    "panzhihua": "攀枝花",
    "luzhou": "泸州",
    "deyang": "德阳",
    "mianyang": "绵阳",
    "guangyuan": "广元",
    "scsuining": "遂宁",
    "neijiang": "内江",
    "leshan": "乐山",
    "nanchong": "南充",
    "meishan": "眉山",
    "yibin": "宜宾",
    "guangan": "广安",
    "dazhou": "达州",
    "yaan": "雅安",
    "bazhong": "巴中",
    "ziyang": "资阳",
    "aba": "阿坝",
    "ganzi": "甘孜",
    "liangshan": "凉山",
    "guiyang": "贵阳",
    "liupanshui": "六盘水",
    "zunyi": "遵义",
    "anshun": "安顺",
    "tongren": "铜仁",
    "qianxinan": "黔西南",
    "bijie": "毕节",
    "qiandongnan": "黔东南",
    "qiannan": "黔南",
    "kunming": "昆明",
    "qujing": "曲靖",
    "yuxi": "玉溪",
    "baoshan": "保山",
    "zhaotong": "昭通",
    "lijiang": "丽江",
    "puer": "普洱",
    "lincang": "临沧",
    "chuxiong": "楚雄",
    "honghe": "红河",
    "wenshan": "文山",
    "xishuangbanna": "西双版纳",
    "dali": "大理",
    "dehong": "德宏",
    "nujiang": "怒江",
    "diqing": "迪庆",
    "lasa": "拉萨",
    "changdu": "昌都",
    "shannan": "山南",
    "rikaze": "日喀则",
    "naqu": "那曲",
    "ali": "阿里",
    "linzhi": "林芝",
    "xian": "西安",
    "tongchuan": "铜川",
    "baoji": "宝鸡",
    "xianyang": "咸阳",
    "weinan": "渭南",
    "yanan": "延安",
    "hanzhong": "汉中",
    "yulin": "榆林",
    "ankang": "安康",
    "shanglv": "商洛",
    "lanzhou": "兰州",
    "jiayuguan": "嘉峪关",
    "jinchang": "金昌",
    "baiyin": "白银",
    "tianshui": "天水",
    "wuwei": "武威",
    "zhangye": "张掖",
    "pingliang": "平凉",
    "jiuquan": "酒泉",
    "gsqingyang": "庆阳",
    "dingxi": "定西",
    "longnan": "陇南",
    "linxia": "临夏",
    "gannan": "甘南",
    "xining": "西宁",
    "haidong": "海东",
    "haibei": "海北",
    "huangnan": "黄南",
    "hainan": "海南",
    "guolv": "果洛",
    "yushu": "玉树",
    "haixi": "海西",
    "yinchuan": "银川",
    "shizuishan": "石嘴山",
    "wuzhong": "吴忠",
    "nxguyuan": "固原",
    "zhongwei": "中卫",
    "wulumuqi": "乌鲁木齐",
    "kelamayi": "克拉玛依",
    "tulufan": "吐鲁番",
    "hami": "哈密",
    "changji": "昌吉",
    "xjbozhou": "博州",
    "xjbazhou": "巴州",
    "akesu": "阿克苏",
    "kezhou": "克州",
    "kashi": "喀什",
    "hetian": "和田",
    "yili": "伊犁",
    "tacheng": "塔城",
    "aletai": "阿勒泰",
    "shihezi": "石河子",
    "wujiaqu": "五家渠",
    "taibei": "台北",
    "taizhong": "台中",
    "gaoxiong": "高雄",
    "xianggang": "香港",
    "aomen": "澳门"
    }

year=['2011','2012','2013','2014','2015','2016','2017','2018','2019']
month=['01','02','03','04','05','06','07','08','09','10','11','12']

ua=UserAgent()

requests_failed=[]
for i in city.keys():
    if os.path.getsize('../mapdata_basic/{}.json'.format(city[i]))!=0:
        print(city[i])
        continue        #排除已爬取过的城市，程序中断之后方便继续
    infor=[]
    days=0
    for m in range(9):
        for n in range(12):
            url='http://www.tianqihoubao.com/lishi/'+i+'/month/{}.html'.format(year[m]+month[n])
            
            trytimes=0
            while(trytimes<20):
                try:
                    headers={"User-Agent":ua.random}        
                    res=requests.get(url=url,headers=headers,timeout=2) #设置超时时间为2s
                    if res.status_code==200:
                        break
                except:
                    trytimes+=1
                    print('{} 请求失败第{}次'.format(city[i]+year[m]+month[n],trytimes))
                    requests_failed.append('{} 请求失败第{}次'.format(city[i]+year[m]+month[n],trytimes))  #输出报错信息
            if trytimes==20:
                break
            
            soup=BeautifulSoup(res.text,'html.parser')
            data_time=soup.select('#content > table > tr > td:nth-child(1) > a')
            data_weather=soup.select('#content > table > tr > td:nth-child(2)')
            data_temperature=soup.select('#content > table > tr > td:nth-child(3)')
            data_wind=soup.select('#content > table > tr > td:nth-child(4)')

            days_temp=days
            for time in data_time:
                t=time.string
                if t!=None:
                    t=t.replace('\n','').replace('\r','').replace(' ','')
                    infor.append({'city':city[i],'time':t,'weather':'','temperature':'','wind':''})
                    days+=1

            count=days_temp
            for weather in data_weather:
                t=weather.string
                if t!=None:
                    t=t.replace('\n','').replace('\r','').replace(' ','')
                    infor[count]['weather']=t
                    count+=1

            count=days_temp
            for temperature in data_temperature:
                t=temperature.string
                if t!=None:
                    t=t.replace('\n','').replace('\r','').replace(' ','')
                    infor[count]['temperature']=t
                    count+=1

            count=days_temp
            for wind in data_wind:
                t=wind.string
                if t!=None:
                    t=t.replace('\n','').replace('\r','').replace(' ','')
                    infor[count]['wind']=t
                    count+=1
    
    json_data=json.dumps(infor,indent=4,ensure_ascii=False)
    with io.open('../mapdata_basic/{}.json'.format(city[i]),'w',encoding='utf-8') as fp:
        fp.write(json_data)

error_data=json.dumps(requests_failed,indent=2,ensure_ascii=False)  #将报错信息整理成一个文档输出，检查是否有城市的信息未被爬取
with io.open('./error_infor.json','w',encoding='utf-8') as ffp:
    ffp.write(error_data)
