## IOT-LED

#### Requirements:
-RGB LED;
-WEMOS ESP-WROOM-32 microcontroller capable of running micropython;
-USB data cable;
-some cables for connecting LED to microcontroller pins;


#### 1. Flashing the microcontroller: 
  1.1 Download the .bin file from terminal: 
- ```wget http://micropython.org/resources/firmware/esp32-20171024-v1.9.2-280-g2305d848.bin```

  1.2 Erase current and flash new file:
- ```sudo esptool.py -p /dev/ttyUSB0 -b 460800 erase_flash```
- ```sudo esptool.py -p /dev/ttyUSB0 -b 460800 write_flash --flash_mode dio 0x1000 esp32-20171024-v1.9.2-280-g2305d848.bin ```


#### 2. Copying python code to microcontroller:
  2.1 Install ampy utility and Copy boot.py file to microcontroller to automatically connect to WLAN with SSID 'itcollege':
- ```pip install adafruit-ampy```
- ```ampy -p /dev/ttyUSB0 put boot.py```

  2.2 Copy main.py file to microcontroller:
- ```ampy -p /dev/ttyUSB0 put main.py```

  2.3 Copy uwebsockets.py file to microcontroller:
- ```ampy -p /dev/ttyUSB0 put uwebsockets.py```


#### 3. Controlling LED
  3.1. Use following command to connect to microcontroller and see feedback
- ```picocom -b115200 /dev/ttyUSB0```

  3.2 Go to http://enos.itcollege.ee/~horunk/iot.html 
  Use the slider to control LED
