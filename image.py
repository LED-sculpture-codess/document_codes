import numpy as np
from PIL import Image
import cv2
import os
fin = np.zeros((16,24))
cap = cv2.VideoCapture('ENVISAGE.mp4')

def bin_to_int(binary_array) :
	l = len(binary_array)
	a = 0
	for i in range(len(binary_array)):
		a = (2*a + binary_array[i])
	if a <= 9 :
		return str(a)
	else :
		return chr(a + ord('A') - 10)

f = open("demofile.txt", "w")

while(cap.isOpened()):
    ret, frame = cap.read()
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im2, contours, -1, (255,255,255), 3)
    cv2.imwrite('cfi1.jpg',im2)
    #img = im2.resize((int(12),int(16)), Image.ANTIALIAS)
    basewidth = 6
    img = Image.open('cfi1.jpg')
    hsize = 16
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('cfi3.jpg')

    test = cv2.imread('cfi3.jpg',0)
    test = 255-test
    _,test1 = cv2.threshold(test,30,255,0)
    T = np.where(test1>0,1,0)
    array = [1,2,4,8]
    for k in range(20):
    	for r in range(16):  #rows    
        	for c in range(3):	#column 
        		for n in range(16) :	#switching
                                for m in range(6):
        	                        f.write(bin_to_int(T[r][c:c+4]))
                                if n < 4 :
                                        f.write('0')
                                        f.write('0')
                               	        f.write('0')
                                        f.write(str(array[n]))
                                elif n < 8 :
                           	        f.write('0')
                           	        f.write('0')
                           	        f.write(str(array[n-4]))
                           	        f.write('0')
                                elif n < 12 :
                                        f.write('0')
                                        f.write(str(array[n-8]))
       	                                f.write('0')
       	                                f.write('0')
                                else :
                                        f.write(str(array[n-12]))        
                                        f.write('0')
                                        f.write('0')        
                                        f.write('0')
    os.system('clear') #cls on windows , clear on linux/mac ox

f.close()
cv2.destroyAllWindows();
