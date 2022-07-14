# 跌倒检测装置
## 依赖
使用Python3 OpenCV-Python 和 Mediapipe实现
## 实现原理
上位机采集数据，进行分析和判断；下位机接受来自于上位机的消息（例如摔倒情况，摔倒时获取的图片），将获取到的图片按照预制的模板，将跌倒情况和图片发送到指定的邮箱。
## 文件说明
①在龙芯2K1000开发版上运行Loongson文件夹内的lx_msg.py脚本，利用socket在内网建立连接。（需预设置Loongson的IP地址）
②上位机运行main.py启动服务（摄像头），当获取到当前监控区域有摔倒情况时，自动拍摄照片，储存并发送到Loongson下位机，由教育派实现预警信息传输。
## 如何使用
### 上位机部分
安装Python3，pip，Opencv-python，mediapipe等依赖
（Debian默认附带python3与python2，需要进行更新）

```
sudo apt-get update
```

```
sudo apt -y upgrade
```
安装pip

```
sudo apt install -y python3-pip
```
安装numpy, cython, pillow

```
sudo pip3 install cython
sudo pip3 install numpy
sudo pip3 install pillow
```
安装开发工具包

```
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```
安装各种依赖

```
sudo apt-get install libhdf5-dev -y

sudo apt-get install libhdf5-serial-dev –y

sudo apt-get install libatlas-base-dev –y

sudo apt-get install libjasper-dev -y

sudo apt-get install libqtgui4 –y

sudo apt-get install libqt4-test –y
```
安装opencv-python

```
sudo pip3 install opencv- python
```
安装Mediapipe

```
sudo pip3 install mediapipe
```
检查Mediapipe是否完成安装

```
#无报错说明成功安装
python3
import mediapipe
```
进行运行测试

```
python3 main.py
```


### 下位机部分
安装Python3 PyEmail（Smtpilb）

```
sudo pip3 install PyEmail
```
进行运行测试

```
cd loongson
python3 lx_msg.py
```
程序显示Wait...表示正在等待上位机的消息，若上位机发送跌倒情况，下位机将显示Fall！！并将从上位机获取照片，本地命名为new_photo.jpg，将次照片通过邮件的形式发送到指定的邮箱内
# 演示
<img width="873" alt="test" src="https://user-images.githubusercontent.com/12545832/179015462-67def089-12ef-4a93-8208-29c2af5ebecb.png">


