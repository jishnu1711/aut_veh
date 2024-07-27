import RPi.GPIO as GPIO
import signal
import sys

counter = 0
PIN = 12

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def count(channel):
    global counter
    counter += 1
    print("Number of pulses:", counter)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Using pull-down resistor

    # Use GPIO.FALLING to detect when the sensor output goes low (object detected)
    GPIO.add_event_detect(PIN, GPIO.FALLING, callback=count,bouncetime=50)

    # Setup signal handling for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

