## ProjectRobot

Aim of this project is to create robot with use of Raspberry Pi 2 and 
following items/functionalities:
- 2 DC motors (with wheels)
- Ultrasonic distance sensor
- Temperature sensor
- Nokia 5100 lcd 
- Wi-fi or RF 
- Camera streaming
- Voice Synth
- Voice control

I will try to apply some machine learning to robot after connecting all necessary modules and electronic equipment. 

### Running project
Currently, the project consists mainly of an application written in Python. It triggers the flask server on port `8765` with which you can control robot's engines and synthesize sound in English and Polish using simple web form.

### Extra dependencies
Because I use clone of RaspberryPi I use modified RPi_GPIO library. But if you want to use original RaspberryPI you can use library from Python Package Index.
You can use `motors.py` if you want to connect RaspberryPI to motors directly or (just like me) you can use Adafruit Motor Shield [Adafruit Motor Shield](https://www.adafruit.com/product/81) and use `mshield.py`.

### Installing 
Project is using Python 3. I prefer to use Python virtual environment but you can just use global libraries.
```sh 
virtualenv -p /usr/bin/python3 py3env
source py3env/bin/activate
pip install -r requirements.txt
```
### License
Some of the ideas of robot functions I taken from Project [https://github.com/sukeesh/Jarvis](https://github.com/sukeesh/Jarvis).
This project is licensed under the MIT License - see the license below.

MIT License

Copyright (c) 2017 Michal Kostewicz <m.kostewicz84@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
