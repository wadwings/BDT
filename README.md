# BDT

## 数据组

### 简要信息

 数据组工作由**阮乐天**与**施远栋**负责，各自爬取16个省、直辖市、自治区中的地级市的天气信息（2011年1月1日至今），数据组文件目录如下：

* get_update.py
* index.json
* mapdata
  * 城市.json
* programs
  * get_index.py
  * crawl_past_sky.py
  * crawl_past_syd.py
  * crawl_2020.py
  * update_today.py
  * update_sky.py

### 索引文件

 程序***get_index.py***由**阮乐天**编写，用于爬取全国的省、市对应信息，并生成索引文件***index.json***
  
### 主体爬取

 程序***crawl_past_syd.py***和***crawl_past_sky.py***分别由**施远栋**和**阮乐天**编写，各自用于爬取16个省、直辖市、自治区自2011.01.01至2019.12.31的天气信息；

 程序***crawl_2020.py***由**施远栋**编写，用于爬取全国2020年1至5月的天气信息；

### 数据更新

 程序***update_sky.py***由**阮乐天**编写，用于更新2020年的天气信息，每次至多更新一个月的数据，缺陷在于更新速度慢；

 程序***update_today***由**施远栋**编写，用于更新当日的天气信息，限制在于只能在当日更新数据，错过便缺失了这一天的数据；

 综合考虑，将***update_syd.py***重命名为***get_update.py***并放在***BDT***目录中，用于更新数据
