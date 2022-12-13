
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem1441201', baudrate=2000000, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)

while True:
    num = input("Enter a number: ")
    print(write_read(num))
