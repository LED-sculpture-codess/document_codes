#this for 3d mesh data
#for conversion of 3d numpy data to data format to be sent to shift registers
def file_size(data_file) :
        import os
        statinfo = os.stat(data_file)
        return statinfo.st_size

def bin_to_int(binary_array) :
	a = 0
	for i in range(len(binary_array)):
		a = (2*a + binary_array[i])
	if a <= 9 :
		return str(a)
	else :
	        return chr(a + ord('A') - 10)
	        
def binstr_to_int(string) :
        l =len(string)
        string = list(string)
        data = []
        for i in range(l) :
                data.append(int(string[i]))
        return bin_to_int(data)

file_name = "rain_pattern.txt"  #enter the required files name
write_file_name = "new_data.txt"

data_file = open(file_name,"r")
store_file = open(write_file_name,"w")

total_bits = file_size(file_name)
print(total_bits)
frame_size = 16*12*6
total_frames = int(total_bits/frame_size)
array = ['E','D','B','7']

for f_no in range(total_frames) :
        bin_data = data_file.read(frame_size)
        for l in range(16) :  #mutiplying factor
                for r in range(16) :  #rows
                        for d in range(6): 
                                for c in range(3):  # column
                                        store_file.write(binstr_to_int(bin_data[192*d+12*r+4*c:192*d+12*r+4*c+4]))
                        if r < 4 :
                                store_file.write('F')
                                store_file.write('F')
                                store_file.write('F')
                                store_file.write(array[r])
                        elif r < 8 :
                                store_file.write('F')
                                store_file.write('F')
                                store_file.write(array[r-8])
                                store_file.write('F')
                        elif r < 12 :
                                store_file.write('F')
                                store_file.write(array[r-12])
                                store_file.write('F')
                                store_file.write('F')
                        else :
                                store_file.write(array[r-16])
                                store_file.write('F')
                                store_file.write('F')
                                store_file.write('F')
data_file.close()
store_file.close()
