import board
import busio
import RPi.GPIO as GPIO
import time
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
try:
	while True:
		ads = ADS.ADS1115(i2c)
		chan = AnalogIn(ads, ADS.P0)
		vol = chan.voltage
		trnc_vol = int(vol*1000)/1000.0
		print(chan.value, trnc_vol)
		time.sleep(0.3)
except KeyboardInterrupt:
	print("hehe heehee")
	GPIO.cleanup()
