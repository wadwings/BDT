# BDT

## 数据组

### 简要信息

 数据组工作由**阮乐天**与**施远栋**负责，各自爬取16个省、直辖市、自治区中的地级市的天气信息（2011年1月1日至今）以及一些进阶数据，数据组文件目录***DATA***内容如下：

* get_update.py
* index_i.json
* mapdata_i
  * 城市.json
* mapdata_basic
  * 城市.json
* mapdata_aqi
  * 城市aqi.json
* programs
  * get_index_i.py
  * get_index.py
  * aqi_sky.py
  * aqi_syd.py
  * i_sky.py
  * i_syd.py
  * crawl_past_sky.py
  * crawl_past_syd.py
  * crawl_2020.py
  * update_today.py
  * update_sky.py

### 索引文件

 程序***get_index.py***由**阮乐天**编写，用于爬取全国的省、市对应信息，并生成索引文件***index.json***;

 程序***get_index_i.py***由**阮乐天**编写，用于爬取世界各洲、国家、城市对应信息，并生成索引文件***index_i.json***
  
### 主体爬取

 程序***crawl_past_syd.py***和***crawl_past_sky.py***分别由**施远栋**和**阮乐天**编写，各自用于爬取16个省、直辖市、自治区自2011.01.01至2019.12.31的天气信息；

 程序***crawl_2020.py***由**施远栋**编写，用于爬取全国2020年1至5月的天气信息；

 数据存储在***mapdata_basic***中

### 进阶数据

* 全国各城市自2014年01月01日至2020年03月31日的空气质量相关数据：
  
  程序***aqi_sky.py***和***aqi_syd.py***分别由**阮乐天**和**施远栋**编写，各自用于爬取16个省、直辖市、自治区的空气质量数据；

  数据存储在***mapdata_aqi***中

* 世界各地2017年及之前几年按月统计的天气数据：

  程序***i_sky.py***和***i_syd.py***分别由**阮乐天**和**施远栋**编写，各自用于爬取2134个外国城市的天气数据；

  由于网页打不开以及数据缺失等原因，最终只有4115个json文件，其中又有920个文件无数据；

  数据存储在***mapdata_i***中

### 数据更新（仅限于基础数据）

 程序***update_sky.py***由**阮乐天**编写，用于更新2020年的天气信息，每次至多更新一个月的数据，缺陷在于更新速度慢；

 程序***update_today***由**施远栋**编写，用于更新当日的天气信息，限制在于只能在当日更新数据，错过便缺失了这一天的数据；

 综合考虑，将***update_syd.py***重命名为***get_update.py***并放在***DATA***目录中，用于更新数据

### JSON文件中的关键字含义

* ***mapdata_basic***中：
  * city：城市名
  * time：日期
  * weather：天气
  * temperature：气温
  * wind：风向
* ***mapdata_aqi***中：
  * city：城市名
  * time：日期
  * level：空气质量等级
  * aqi：空气质量指数
  * rank：当日AQI排名
  * PM2.5，PM10，SO2，NO2，O3：单位 μg/m3
  * CO：单位 mg/m3
* ***mapdata_i***中：
  * city：城市名
  * time：月份
  * max：最高气温
  * min：最低气温
  * a_max：平均最高气温
  * a_min：平均最低气温
  * sunny：晴天天数
  * rainy：雨天天数
  * cloudy：阴天/多云天数
  * snowy：雪天天数
