import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)
time.sleep(2)

#def makeOrder(pin2, pin3, pin4, pin5, pin7, pin8, pin9, pin10):
pin2 = "0"
pin3 = "1"
pin4 = "0"
pin5 = "1"
pin7 = "1"
pin8 = "1"
pin9 = "0"
pin10 = "0"

command = (pin2 + ',' + pin3 + ',' + pin4 + ',' + pin5 + ',' + pin7 + ',' + pin8 + ',' + pin9 + ',' + pin10 + '\n')
print command

ser.write(command.encode())
