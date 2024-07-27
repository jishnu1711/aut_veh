import board
import busio
import RPi.GPIO as GPIO
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

try:
    i2c = busio.I2C(board.SCL, board.SDA)
    GPIO.setmode(GPIO.BCM)  # Set GPIO mode

    while True:
        print("loop loop loop")
        ads = ADS.ADS1115(i2c)
        chan = AnalogIn(ads, ADS.P0)
        vol = chan.voltage
        trnc_vol = round(vol, 3)  # Round to 3 decimal places

        if trnc_vol > 2.539:
            print("forward da punde")
        elif trnc_vol < 2.535:
            print("backward da punde")
        else:
            print("nope")

        time.sleep(1)  # Adjust sleep time as needed

except KeyboardInterrupt:
    print("Program interrupted by user")
    GPIO.cleanup()  # Clean up GPIO on interrupt
