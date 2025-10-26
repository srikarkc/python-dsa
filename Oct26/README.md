# This day is going to be a bit different

I'm working from my Robotics workstation.

## Arduino UNO R4 WiFi

[The tech specs for the board are available here](https://docs.arduino.cc/hardware/uno-r4-wifi/)

[Doc that I'm folloing for learning](https://docs.arduino.cc/)

### Install Arudino IDE

Downloaded the Zip file and placed into /usr/local/bin

### Overview of Arduino Code

There are 2 main functions --> `setup()` and the `loop()`

The `setup()` function runs once at startup while the `loop()` function runs repeatedly forever.

Example code you would put into the setup function:

```C++
pinMode(LED_BUILTIN, OUTPUT);
```

Pin Modes can be either `OUTPUT` or `INPUT`.

#### Step 1 - Make an LED on the Arduino blink

Arduino programming is C++ simplified for microcontrollers.

The Arduino IDE converts your code into C++, compiles it, and uploads it to the tiny computer (Arduino).

The program then runs on the board - no OS, no FileSystem, just your code running directly on the hardware.

#### Step 2 - Connecting to WiFi

There's a WiFi library called 'WiFiS3' that needs to be imported. It can be done in the following manner:

`#include <WiFiS3.h>` instead of the Pythonic way of `from <library> import module`

There was a learning opportunity here, I was trying to print the macAddress() using the `Serial.println(WiFi.macAddress())` but was getting the following error:

```bash
note: candidate: uint8_t* CWifi::macAddress(uint8_t*)
     uint8_t* macAddress(uint8_t* mac);
```

This is because the WiFiS3 library is returning a byte array and not a String directly. The following code worked instead:

```C++
uint8_t mac[6];
WiFi.macAddress(mac);

Serial.print("MAC: ");
for (int i = 0; i < 6; i++) {
  if (mac[i] < 16) Serial.print('0'); // leading zero for single hex digits
  Serial.print(mac[i], HEX);
  if (i < 5) Serial.print(':');
}
Serial.println();
```
