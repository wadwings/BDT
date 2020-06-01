# Hadoop平台搭建指导

1. 安装VMware
2. 配置虚拟机Ubuntu
3. Hadoop安装教程&单机/伪分布式搭建
4. 搭建Hadoop集群

> ## 1.安装VMware

[VMware 15.5 Pro](https://www.onlinedown.net/soft/2062.htm)

1. 安装位置默认在C盘下，在这里我选择安装在F盘，安装路径尽量不要有中文。

2. 安装成功后，第一次运行程序会要求输入密钥，这个可以自己百度或试试下列。   

   激活密钥许可证VMware Workstation Pro 15  
   激活许可证  
   UY758-0RXEQ-M81WP-8ZM7Z-Y3HDA  
   VF750-4MX5Q-488DQ-9WZE9-ZY2D6  
   UU54R-FVD91-488PP-7NNGC-ZFAX6  
   YC74H-FGF92-081VZ-R5QNG-P6RY4  
   YC34H-6WWDK-085MQ-JYPNX-NZRA2  

3. 完成

> ## 2.配置虚拟机Ubuntu

[Ubuntu 16.04](http://mirrors.163.com/ubuntu-releases/16.04/)

1. 选则[^ubuntu-16.04.6-desktop-amd64.iso]下载，因为在官网下载速度太慢。

[^ubuntu-16.04.6-desktop-amd64.iso]: ubuntu-16.04.6 x64位镜像文件

2. 依照<https://blog.csdn.net/wang_624/article/details/90347274>安装Ubuntu
3. 配置[^VMTool]<https://jingyan.baidu.com/article/bad08e1ef759f209c85121de.html>

[^VMTool]: VMWARE tools是虚拟机自带的软件，其中包括：虚拟机中的设备驱动、实机与虚拟机之间的文件夹共享、还有一些开发功能的插件等。安装了vmware tools，虚拟机就可以打开DX3D的支持，鼠标想移出虚拟机也不需要按组合键，文件可以从主机直接拖动复制到虚拟机里面，虚拟机的分辨率也会自动跟随窗口调整而变化，拓展了虚拟机的功能，简化了主机和虚拟机之间的操作。

> ## 3.Hadoop安装教程&单机/伪分布式搭建

直接依照<http://dblab.xmu.edu.cn/blog/install-hadoop/>

> ## 4.搭建Hadoop集群

1. 设置网络链接为**Bridged桥接模式**，并设置静态IP
   - 由于后面集群互联需要各独自联网，这里VMware中虚拟机-设置-网络适配器为**Bridged桥接模式**，并复制物理网络连接状态。
   - 编辑-虚拟网络编辑器-更改设置-[^VMnet0]-改为桥接模式
   - 接下来参考<https://blog.csdn.net/maizousidemao/article/details/79116225>
   - 配置完后，重启网络不能更改IP地址的话，试试重启虚拟机`sudo reboot`

[^VMnet0]: 桥接模式默认使用的虚拟网卡  （ 相当于物理主机和虚拟机的桥梁，配置其IP可以使两者进行通信）

2. 依照<http://dblab.xmu.edu.cn/blog/install-hadoop-cluster/>搭建即可

3. hadoop 中常用命令，又能力也可参照[官方文档](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html)

> 1. 请求命令帮助
>
> ```
> hdfs dfs -help [command] 后面不加[command]是查询所有的命令，加是查询某一特定命令
> ```
>
> 2. 查看指定目录下内容
>
> ```
> hdfs dfs –ls [-R] [文件目录] 加-R表示递归列出目录
> ```
>
> 3. 打开某个已存在文件
>
> ```
> hdfs dfs –cat [file_path]
> ```
>
> 4. 将本地文件存储至hadoop
>
> ```
> hdfs dfs –put [本地地址] [hadoop目录]
> ```
>
> 5. 将本地文件夹存储至hadoop
>
> ```
> hdfs dfs –put [本地目录] [hadoop目录]
> hdfs dfs –put /home/t/dir_name /user/t
> ```
>
>    (dir_name是文件夹名)
>
> 6. 将hadoop上某个文件down至本地已有目录下
>
> ```
>  hadoop dfs -get [文件目录] [本地目录]
> 
>  hadoop dfs –get /user/t/ok.txt /home/t
> ```
>
> 7. 删除hadoop上指定文件
>
> ```
>  hdfs  dfs –rm [文件地址]
> 
>  hdfs dfs –rm /user/t/ok.txt
> ```
>
> 8.  删除hadoop上指定文件夹（包含子目录等）
>
> ```
>  hdfs dfs –rm [目录地址]
> 
>  hdfs dfs –rmr /user/t
> ```
>
> 9. 在hadoop指定目录内创建新目录
>
> ```
>   hdfs dfs –mkdir /user/t
> 
>   hdfs  dfs -mkdir - p /user/centos/hadoop
> ```
>
> 10. 在hadoop指定目录下新建一个空文件
>
> ```
> 使用touchz命令：
> 
> hdfs dfs  -touchz  /user/new.txt
> ```
>
> 11. 将hadoop上某个文件重命名
>
> ```
> 使用mv命令:
> hdfs dfs –mv  /user/test.txt  /user/ok.txt   （将test.txt重命名为ok.txt）
> ```
>
> 12. 将hadoop指定目录下所有内容保存为一个文件，同时down至本地
>
> ```
> hdfs dfs –getmerge /user /home/t
> ```
>
> 13. 将正在运行的hadoop作业kill掉
>
> ```
> hadoop job –kill  [job-id]
> ```
>
> 
