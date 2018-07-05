#!/usr/bin/env python3
# George Trieu
# Fan Control Script for Raspberry Pi
# Heavily modified from script by Edoardo Paolo Scalafiotti
# 07-04-2018
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

fanPin = 18 # the GPIO pin we
maxTMP = 50 # The maximum temperature in Celsius after which we trigger the fan
minTMP = 40 # The temperature where the fan will turn off

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    return temp
def getTEMP():
    CPU_temp = float(getCPUtemperature())
    if CPU_temp>maxTMP:
        GPIO.output(fanPin, True)
    elif CPU_temp<minTMP:
        GPIO.output(fanPin, False)
    return()
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fanPin,GPIO.OUT)
    GPIO.setwarnings(False)
    while True:
        getTEMP()
        sleep(5) # Read the temperature every 5 sec
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
