运行python例程
安装函数库
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
安装函数库（python2）
sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install python-pil
sudo apt-get install python-numpy
sudo pip install RPi.GPIO
sudo pip install spidev
下载程序（已下载可跳过）
sudo apt-get install p7zip-full
wget  https://files.waveshare.net/wiki/w/upload/3/39/E-Paper_code.7z
7z x E-Paper_code.7z -O./e-Paper
cd e-Paper/RaspberryPi_JetsonNano/
通过 GitHub 下载程序（备用方式，已下载可跳过）
目前访问 GitHub 并不是很流畅，建议使用上面的方法从我们官网下载。
git clone https://github.com/waveshare/e-Paper.git
cd e-Paper/RaspberryPi_JetsonNano/
运行程序
# 确保在 e-Paper/RaspberryPi_JetsonNano/ 位置
cd python/examples/
python3 epd_7in3f_test.py


 
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



