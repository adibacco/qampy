import sys
import time
import os
import numpy as np
from math import pi as pi
from scipy import signal as sig

MAX_SIG = 30000

inputfile = 'ssb_30k_50M_0806-16384-.bin'
inputfile = sys.argv[1]
save_file = 1

try:
    off_i = float(sys.argv[2])
except IndexError:
    off_i = 0
    save_file = 0

try:
    off_q = float(sys.argv[3])
except IndexError:
    off_q = 0
    save_file = 0



try:
    amp_i = float(sys.argv[4])
except IndexError:
    amp_i = 1.0
    save_file = 0

try:
    amp_q = float(sys.argv[5])
except IndexError:
    amp_q = 1.0
    save_file = 0



iq = np.fromfile(inputfile, dtype = np.dtype('<i2'))

i = iq[::2] 
q = iq[1::2] 

print('Input signal')
max_i = np.max(i)
min_i = np.min(i)
max_q = np.max(q)
min_q = np.min(q)

mean_i = np.mean(i)
mean_q = np.mean(q)
print('max I ' + str(max_i) + ' min I ' + str(min_i) + ' mean I ' + str(mean_i))
print('max Q ' + str(max_q) + ' min Q ' + str(min_q) + ' mean Q ' + str(mean_q))

l = len(iq)



io = i*amp_i 
qo = q*amp_q 




io = io + off_i
qo = qo + off_q

max_io = np.max(io);
min_io = np.min(io);
max_qo = np.max(qo);
min_qo = np.min(qo);




if (save_file == 0):
    exit()

print('Output signal')
max_i = np.max(io)
min_i = np.min(io)
max_q = np.max(qo)
min_q = np.min(qo)
mean_i = np.mean(io)
mean_q = np.mean(qo)
print('max I ' + str(max_i) + ' min I ' + str(min_i) +  ' mean I ' + str(mean_i))
print('max Q ' + str(max_q) + ' min Q ' + str(min_q) +  ' mean Q ' + str(mean_q))

iq_o = np.vstack((io, qo)).ravel('F')
dt = np.dtype('<i2')  
iq_o.astype(dtype=dt).tofile('mod_'+inputfile)







