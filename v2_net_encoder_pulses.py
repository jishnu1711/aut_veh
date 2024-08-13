import RPi.GPIO as GPIO
import time
import signal
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import board
import busio

counter_r = 0
counter_l = 0
r_enc = 23
l_enc = 24

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def count_l(channel):
    global counter_l
    global trnc_vol_l

    if trnc_vol_l < 2.547:
        counter_l += 1
        print(f'frwrd: {counter_l}')
    elif trnc_vol_l > 2.551:
        counter_l -= 1
        print(f'bkwrd: {counter_l}')
    else:
        print(f'rest: {counter_l}')

def count_r(channel):
    global counter_r
    global trnc_vol_r

    if trnc_vol_r > 2.484:
        counter_r += 1
        print(f'frwrd: {counter_r}')
    elif trnc_vol_r < 2.476:
        counter_r -= 1
        print(f'bkwrd: {counter_r}')
    else:
        print(f'rest: {counter_r}')

if __name__ == '__main__':
    i2c = busio.I2C(board.SCL, board.SDA)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(r_enc, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(l_enc, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(l_enc, GPIO.FALLING, callback=count_l, bouncetime=200)
    GPIO.add_event_detect(r_enc, GPIO.FALLING, callback=count_r, bouncetime=200)

    while True:
        ads = ADS.ADS1115(i2c)
        chan_l = AnalogIn(ads, ADS.P1)
        chan_r = AnalogIn(ads, ADS.P0)
        vol_l = chan_l.voltage
        vol_r = chan_r.voltage
        trnc_vol_l = round(vol_l, 3)
        trnc_vol_r = round(vol_r, 3)
        signal.signal(signal.SIGINT, signal_handler)
        signal.pause()
