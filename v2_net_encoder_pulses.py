import RPi.GPIO as GPIO
import time 
import signal
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

counter_r = 0
counter_l = 0
r_enc = 23
l_enc = 24

def signal_handler(sig,frame:)
	GPIO.cleanu()
	sys.exit(0)
def count(channel):
	global counter 
	
