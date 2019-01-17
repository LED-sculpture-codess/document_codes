import numpy as np

def print_frame(frame,file_id) :
        for d in np.arange(6) :
                for r in np.arange(16) :
                        for c in np.arange(12) :
                                if frame[5 - d][15 - r][c] == 1 :
                                        file_id.write('1')
                                else :
                                        file_id.write('0')       
                                        
data_file = open("rain_pattern.txt","w")

frame = np.zeros([6,16,12]) #d, r, c

for i in np.arange(42) :
        if i :
                for r in np.arange(15) :
                        for d in np.arange(6) :
                                for c in np.arange(12) :
                                        frame[d][r+1][c] = frame[d][r][c] 
                        
        data = np.random.randint(2,size = (6,12))
        for d in np.arange(6) :
                for c in np.arange(12) :
                        frame[d][0][c] = data[d][c]
        print_frame(frame,data_file)
