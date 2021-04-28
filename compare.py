import numpy as np
from scipy import signal


plot = True
if plot:
    import matplotlib.pyplot as plt


infiletx= 'tx_qpsk_30mbd_seq_0213-16128-112896-.bin'

iqt = np.fromfile(infiletx, dtype = np.dtype('<i2'))


it = iqt[::2]/2
qt = iqt[1::2]/2

it = signal.resample_poly(it, 1, 2)
qt = signal.resample_poly(qt, 1, 2)


infilerx= 'rx_qpsk_30mbd_seq_0213-16128-112896-.bin'

iqr = np.fromfile(infilerx, dtype = np.dtype('<i2'))

ir = iqr[::2]
ir = ir - np.mean(ir)
qr = iqr[1::2]
qr = qr - np.mean(qr)

plt.plot(it)
plt.plot(ir)
plt.show()


