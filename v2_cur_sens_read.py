import board
import busio
import RPi.GPIO as GPIO
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADS1115
ads = ADS.ADS1115(i2c)

# Initialize AnalogIn for two channels
chan1 = AnalogIn(ads, ADS.P0)
chan2 = AnalogIn(ads, ADS.P1)

try:
    while True:
        # Read values from both channels
        vol1 = chan1.voltage
        time.sleep(0.05)
        vol2 = chan2.voltage
        
        # Truncate values to 3 decimal places
        trnc_vol1 = int(vol1 * 1000) / 1000.0
        trnc_vol2 = int(vol2 * 1000) / 1000.0
        
        # Print the results
        print(f"A:  {trnc_vol1}V")
        print(f"B:  {trnc_vol2}V")
        print()
        
        # Wait for a bit before the next reading
        time.sleep(0.5)

except KeyboardInterrupt:
    print("KeyboardInterrupt detected. Exiting...")
    GPIO.cleanup()
