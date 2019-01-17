import numpy as np

def print_frame(frame,file_id) :
        for d in np.arange(6) :
                for r in np.arange(16) :
                        for c in np.arange(12) :
                                if frame[5 - d][15 - r][c] == 1 :
                                        file_id.write('1')
                                else :
                                        file_id.write('0')                                

sin = [[8,12,15,15,15,12,8,4,1,0,1,4],[8,12,14,15,14,12,8,5,2,1,2,5],[8,11,13,14,13,11,8,5,3,2,3,5],[8,11,12,13,12,11,8,6,4,3,4,6,8],[8,10,11,12,11,10,8,6,5,4,5,6],[8,9,10,10,10,9,8,7,6,6,6,7]]

data_file = open("wave_file","w")

frame = np.zeros([6,16,12])  #d,r,c
for i in np.arange(12) :
        for d in np.arange(6) :
                for c in np.arange(12) :
                     frame[d][sin[i + d - int((i+d)/6)*6][i + c - int((i+c)/12)*12]][c]
        print_frame(frame,data_file)
