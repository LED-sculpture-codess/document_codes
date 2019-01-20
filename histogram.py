import matplotlib.pyplot as plt
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
rate ,data = wav.read('g_tdd_120_01.wav')    #reading the data using scipy.io.wavfile module

nframe = data.shape[0] 		#no of frames in the audio file
T = 1/rate	        	#time diff between two samples
dt = 0.05       		#sample timewidth for window of shortFFT
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
	a = []
	for j in np.arange(0,20000,2500) :
		max_str = max_in(j, j+2000, sound_data)
		a.append(max_str)
	print(a)
	x = np.arange(8)
	plt.clf()
	plt.hold(True)
	plt.bar(x, a) 
	plt.pause(0.01)
	plt.hold(False)
	continue
