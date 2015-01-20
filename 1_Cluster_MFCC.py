import pickle
from Vivek import kMeans as km
import numpy as np
import wave
from scipy.io import wavfile
import random

# song = wavfile.read('RC7_July_06_2009_38840406_1.wav')
# print song[1].shape[0]*1.0/song[0]

data = pickle.load(open("mfccDumpMix_3.p","rb"))

count=0
input_data = []
input_data = np.asarray(input_data)
parts = data.keys()
random.shuffle(parts)

for part in parts:
    count+=1
    
    #print part
    #print len(data[part])
#     for row in (data[part]):
#         print row
    
#    break
    input_data = np.asarray( input_data.tolist() + data[part].tolist() )
    
    print count
    if (count>=1):
        break
 

 
    
print "input Data: " 
print len(input_data   )
print input_data

for i in xrange (2,25,1):
        result =   km.euclidian_k_means(np.asarray(input_data), i,'euclidean')
        
        print result
        
