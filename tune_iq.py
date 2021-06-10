import sys
import time
import os
import numpy as np
from math import pi as pi
from scipy import signal as sig


inputfile = 'ssb_30k_50M_0806-16384-.bin'
inputfile = sys.argv[1]
off_i = float(sys.argv[2])
off_q = float(sys.argv[3])

try:
    amp_i = float(sys.argv[4])
except IndexError:
    amp_i = 1.0

try:
    amp_q = float(sys.argv[5])
except IndexError:
    amp_q = 1.0



iq = np.fromfile(inputfile, dtype = np.dtype('<i2'))

i = iq[::2] 
q = iq[1::2] 

print('Input signal')
max_i = np.max(i)
max_q = np.max(q)
mean_i = np.mean(i)
mean_q = np.mean(q)
print('max I ' + str(max_i) + ' mean I ' + str(mean_i))
print('max Q ' + str(max_q) + ' mean Q ' + str(mean_q))

l = len(iq)

io = i*amp_i + off_i
qo = q*amp_q + off_q

print('Output signal')
max_i = np.max(io)
max_q = np.max(qo)
mean_i = np.mean(io)
mean_q = np.mean(qo)
print('max I ' + str(max_i) + ' mean I ' + str(mean_i))
print('max Q ' + str(max_q) + ' mean Q ' + str(mean_q))

iq_o = np.vstack((io, qo)).ravel('F')
dt = np.dtype('<i2')  
iq_o.astype(dtype=dt).tofile('mod_'+inputfile)







