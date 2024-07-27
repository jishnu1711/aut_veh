import board
import busio
import RPi.GPIO as GPIO
import time
import signal
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

counter = 0
PIN = 12

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def count(channel):
    global counter
    global trnc_vol
    if trnc_vol>2.533:
        counter += 1
        print("forward net pulses:", counter)
    elif trnc_vol<2.527:
        counter -= 1
        print("backward net pulses: ", counter)
    else :
        counter += 0
        print("constant net pulses: ", counter)

if __name__ == '__main__':
    i2c = busio.I2C(board.SCL, board.SDA)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Using pull-down>

    # Use GPIO.FALLING to detect when the sensor output goes low (object >
    GPIO.add_event_detect(PIN, GPIO.FALLING, callback=count,bouncetime=50)
    while True:
        ads = ADS.ADS1115(i2c)
        chan = AnalogIn(ads, ADS.P0)
        vol = chan.voltage
        trnc_vol = round(vol, 3)  # Round to 3 decimal places

        #if trnc_vol > 2.539:
        #    print("forward da punde")
        #elif trnc_vol < 2.535:
        #    print("backward da punde")
        #else:
        #    print("nope")

 # Setup signal handling for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
