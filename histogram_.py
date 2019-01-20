import matplotlib.pyplot as plt
from time import sleep,time 
import numpy as np
import scipy.io.wavfile as wav
from scipy.fftpack import fft, fftfreq, fftshift

def max_in(fmin , fmax, data) :
	d = { }
	for i in np.arange(fmin,fmax+1,40) :
		d[i] = data[i]
	v = list(d.values())
	max_value = max(v)
	return 	max_value
								
rate ,data = wav.read('despacito_1_min.wav')    #reading the data using scipy.io.wavfile module

nframe = data.shape[0] 		#no of frames in the audio file
T = 1/rate	        	#time diff between two samples
dt = 0.005       		#sample timewidth for window of shortFFT
nsamp = int((dt)/T)     	#no of sample taken in one window
ymax = max(fft(data))

x = np.arange(0,20020,20)
a = np.split(x,[3, 11, 26, 51, 101, 251, 501, 1001])

glob_b =[]
array = []
'''to find the array of the frequency strength in the given data'''
for i in np.arange(0,nframe,nsamp) : 
	d = data[i:(i+nsamp)]	
	f = fftfreq(nsamp,T)     #creates discrete freqranging from -20,000 to 20,000
	f = fftfreq(nsamp,T)     #creates discrete freqranging from -20,000 to 20,000
	Y = fft(d)       #creates fft with 40000 values
	Y = fftshift(Y)
	f = fftshift(f)
	Y = np.abs(Y)     #from data it is removing imaginary part of the data
	sound_data = dict(zip(f,Y))
	b = [] 
	for j in np.arange(8) :
		lo = len(a[j])
		max_str = max_in(min(a[j]), max(a[j]), sound_data)
		b.append(max_str)
		glob_b.append(max_str)
	print(b)
	array.append(b)	

glob_max_stre = max(glob_b)

total_frame = len(array)
'''using the data found above plotting the graph'''
start_time = time()
for i in np.arange(total_frame) :
	x = np.arange(8)
	plt.clf()
	plt.hold(True)
	plt.bar(x, array[i]) 
	plt.hold(False)
	plt.ylim(0,glob_max_stre)
	plt.pause(0.00001)
	continue
end_time = time()
print()
print()
print()
print(end_time-start_time)
print()
print()
print()
