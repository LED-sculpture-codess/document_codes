#because of problem sending data to arduino properly didnt usedthis one

import serial # you need to install the pySerial :pyserial.sourceforge.net
from time import sleep 
import numpy as np
import scipy.io.wavfile as wav
from scipy.fftpack import fft, fftfreq, fftshift

def max_in(fmin , fmax, data) :
	d = { }
	for i in np.arange(fmin,fmax,20) :
		d[i] = data[i]
	v = list(d.values())
	return max(v)	
								
arduino = serial.Serial('/dev/ttyACM0', 9600)      # your Serial port should be different!
sleep(2)   #waits for 2s
print('connection established...')
rate ,data = wav.read('g_tdd_120_01.wav')    #reading the data using scipy.io.wavfile module

nframe = data.shape[0] 		#no of frames in the audio file
T = 1/rate	        	#time diff between two samples
dt = 0.005       		#sample timewidth for window of shortFFT
nsamp = int((dt)/T)     	#no of sample taken in one window
ymax = max(fft(data))
for i in np.arange(0,nframe,nsamp) :	#loop for drawing graph of each window
	d = data[i:(i+nsamp)]	
	f = fftfreq(nsamp,T)     #creates discrete freqranging from -20,000 to 20,000
	Y = fft(d)       #creates fft with 40000 values
	Y = fftshift(Y)
	f = fftshift(f)
	Y = np.abs(Y)     #from data it is removing imaginary part of the data
	sound_data = dict(zip(f,Y))
	for j in np.arange(0,20000,2500) :
		max_str = max_in(j, j+2500, sound_data)
		if max_str > ymax/1000 :
			arduino.write(b'H')
			print(b'H')
		elif max_str < ymax/1000 :
			arduino.write(b'L')
			print(b'L')
	sleep(0.06)
arduino.close()
