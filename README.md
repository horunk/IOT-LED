# IOT-LED
IOT LED project files


1. Flashing the microcontroller:
1.1 Download the .bin file:

1.2 Erase current and flash new file

2.1 Install ampy utility and Copy boot.py file to microcontroller to automatically connect to WLAN with SSID 'itcollege'
pip install adafruit-ampy # Install Adafruit MicroPython Tool
ampy -p /dev/ttyUSB0 put boot.py # Upload boot.py over UART
