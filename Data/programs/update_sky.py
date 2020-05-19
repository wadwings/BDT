import io
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def isavilable(n):
    ua=UserAgent()
    headers={'User-Agent':ua.random}
    url='http://www.tianqihoubao.com/lishi/'+i+'/month/{}.html'.format(str(n))
    trytimes=0
    while(trytimes<6):
        try:      
            res=requests.get(url=url,headers=headers,timeout=2) #设置超时时间为1s
            if res.status_code==200:
                break
        except:
            trytimes+=1
    soup=BeautifulSoup(res.text,'html.parser')
    t=soup.select('#content > h1')
    if t[0].string=='天气后报':
        return 0
    else:
        return 1
    if trytimes==6:
        return -1

def updated(soup,n):
    data=soup.select('#content > table > tr:nth-child({})'.format(str(n)))
    if data==[]:
        return 0
    else:
        return 1

def getsoup(url):
    ua=UserAgent()
    headers={'User-Agent':ua.random}
    trytimes=0
    while(trytimes<10):
        try:      
            res=requests.get(url=url,headers=headers,timeout=2) #设置超时时间为2s
            if res.status_code==200:
                break
        except:
            trytimes+=1
    if trytimes==10:
        print('更新失败，请重试')
        return -1
    else:
        soup=BeautifulSoup(res.text,'html.parser')
        return soup

def getinfor(city_s,infor,soup,date):
    while updated(soup,int(date+2))==1:
        data_time=soup.select('#content > table > tr:nth-child({}) > td:nth-child(1) > a'.format(str(int(date)+2)))
        data_weather=soup.select('#content > table > tr:nth-child({}) > td:nth-child(2)'.format(str(int(date)+2)))
        data_temperature=soup.select('#content > table > tr:nth-child({}) > td:nth-child(3)'.format(str(int(date)+2)))
        data_wind=soup.select('#content > table > tr:nth-child({}) > td:nth-child(4)'.format(str(int(date)+2)))
        infor.append({'city':city_s,'time':data_time,'weather':data_weather,'temperature':data_temperature,'wind':data_wind})
        date+=1
    return infor

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
    "zhumadian": "驻马店",
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


for i in city.keys():
    with io.open('../mapdata/{}.json'.format(city[i]),'r',encoding='utf-8') as readf:
        infor=json.load(readf)
    time=infor[-1]['time']
    date=time[:time.find('日')][-2:]
    month=time[:time.find('月')][-2:]
    year=time[:time.find('年')]

    url='http://www.tianqihoubao.com/lishi/'+i+'/month/{}.html'.format(year+month)  
    soup=getsoup(url)
    if soup==-1:
        break
    if updated(soup,int(date)+2)==0:
        _bool=isavilable(int(year+month)+1)
        if _bool==0:
            print('{} 已更新'.format(city[i]))
            continue
        elif _bool==-1:
            print('更新失败，请重试')
            break
        else:
            url='http://www.tianqihoubao.com/lishi/'+i+'/month/{}.html'.format(str(int(year+month)+1))
            soup=getsoup(url)
            json_infor=json.dumps(getinfor(city[i],infor,soup,0),indent=4,ensure_ascii=False)
            with io.open('../mapdata/{}.json'.format(city[i]),'w+',encoding='utf-8') as wf:
                wf.write(json_infor)
            print('{} 已更新'.format(city[i]))
            continue
    else:
        json_infor=json.dumps(getinfor(city[i],infor,soup,date),indent=4,ensure_ascii=False)
        with io.open('../mapdata/{}.json'.format(city[i]),'w+',encoding='utf-8') as wf:
            wf.write(json_infor)
        print('{} 已更新'.format(city[i]))
        continue
print('\n完成')