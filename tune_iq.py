import sys
import time
import os
import numpy as np
from math import pi as pi
from scipy import signal as sig
import matplotlib.pyplot as plt


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
l = len(iq)

io = i*amp_i + off_i
qo = q*amp_q + off_q

iq_o = np.vstack((io, qo)).ravel('F')
dt = np.dtype('<i2')  
iq_o.astype(dtype=dt).tofile('mod-'+inputfile)







