#!/usr/bin/python

import sys, subprocess, getopt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.Board)

pins = {
	PSU : 5,
	ELC : 8,
	LED : 7,
	FAN : 10
}
def init():
	GPIO.setup(pins[PSU], GPIO.OUT, initial=GPIO.HIGH)
	GPIO.setup(pins[ELC], GPIO.OUT)
	led = GPIO.PWM(pins[LED], 120);
	fan = GPIO.PWM(pins[FAN], 120);
	led.start(0);
	fan.start(0);

def start():
	GPIO.output(pins[PSU], 0)
	GPIO.output(pins[ELC], 1)
	led.ChangeDutyCycle(100);
	fan.ChangeDutyCylce(100);
	sys.exit(0)

def stop():
	GPIO.output(pins[PSU], 1)
	GPIO.output(pins[ELC], 0)
	led.ChangeDutyCylce(0)
	fan.ChangedDutyCycle(0)
	sys.exit(0)

def led(dc):
	led.ChangeDutyCycle(dc)
	sys.exit(0)

def fan(dc):
	fan.ChangeDutyCycle(dc)
	sys.exit(0)

opts, args = getopt.getopt(sys.argv, "")
if args[1] == "on":
	start()

if args[1] == "off":
	stop()

if args[1] == "leds":
	led(arg[2]*100)

if args[1] == "fan":
	fan(arg[2]*100)


