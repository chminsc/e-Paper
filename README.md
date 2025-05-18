开启SPI接口
打开树莓派终端，输入以下指令进入配置界面：
sudo raspi-config
选择Interfacing Options -> SPI -> Yes 开启SPI接口
RPI open spi.png
重启树莓派：
sudo reboot
检查 /boot/config.txt，可以看到 'dtparam=spi=on' 已被写入
RPI open spi 1.jpg
为了确保 SPI 没有被占用，建议其他的驱动覆盖暂时先关闭。可以使用 ls /dev/spi* 来检查 SPI 占用情况，终端输出 /dev/spidev0.0 和 /dev/spidev0.1 表示 SPI 情况正常
RPI open spi 2.jpg


运行python例程
# 安装函数库
sudo apt-get update  
sudo apt-get install python3-pip  
sudo apt-get install python3-pil  
sudo apt-get install python3-numpy  
sudo pip3 install RPi.GPIO  
sudo pip3 install spidev  

# 通过 GitHub 下载程序（备用方式，已下载可跳过）
git clone https://github.com/waveshare/e-Paper.git  

运行程序
# 确保在 e-Paper位置
cd python/programs/  
python3 refreshimages.py 

图片处理：
jpg的landscape图像放在images目录，然执行jpg2bmp.py程序即可。之前不需要裁切（程序自动裁切）

 
 # e-Paper  
waveshare electronics
![waveshare_logo.png](waveshare_logo.png)

## 中文:  
Jetson Nano、Raspberry Pi、Arduino、STM32例程
* RaspberryPi_JetsonNano  
    > C
    > Python 
* Arduino:  
    > Arduino UNO  
* STM32:  
    > STM32F103ZET6 
    
更多资料请在官网上搜索:  
http://www.waveshare.net


## English:  
Jetson Nano、Raspberry Pi、Arduino、STM32 Demo:  
* RaspberryPi_JetsonNano:  
    > C
    > Python
* Arduino:  
    > Arduino UNO  
* STM32:  
    > STM32F103ZET6 
    
For more information, please search on the official website:   
https://www.waveshare.com



