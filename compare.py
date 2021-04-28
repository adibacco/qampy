import numpy as np
from scipy import signal


plot = True
if plot:
    import matplotlib.pyplot as plt


infiletx= 'tx_qpsk_30mbd_seq_0213.bin'

iqt = np.fromfile(infiletx, dtype = np.dtype('<i2'))

iqt = iqt / 2
signal.resample_poly(iqt, 1, 2)

it = iqt[::2]/4
qt = iqt[1::2]/4

infilerx= 'rx_qpsk_30mbd_seq_0213.bin'

iqr = np.fromfile(infilerx, dtype = np.dtype('<i2'))

ir = iqr[::2]
ir = ir - np.mean(ir)
qr = iqr[1::2]
qr = qr - np.mean(qr)

plt.plot(it)
plt.plot(ir)
plt.show()


