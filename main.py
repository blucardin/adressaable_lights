

import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem144401', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)



while True:
    num = input("Enter a number: ")
    write_read(num)



