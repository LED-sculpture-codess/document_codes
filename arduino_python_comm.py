import serial
from time import sleep

arduino = serial.Serial('/dev/ttyACM0',9600)

sleep(2)
print('connection established')

def sender(data) :
	print(bin(data))
	for i in range(12) :
		if data & 1<<i :
			arduino.write(b'H')
			print(b'h')
		else : 
			print(b'l')
			arduino.write(b'L')
data = 0b0000000011111111
	

