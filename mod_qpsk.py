import numpy as np
import sys
from scipy import signal

plot = True
if plot:
    import matplotlib.pyplot as plt


def replicate(max_len, i, q):

    blen = len(i)*2*2

    i = np.tile(i, max_len // blen)
    q = np.tile(q, max_len // blen)

    return [i, q]


def trim_signal(max_samples, i, q):
    i = i[99::]
    q = q[99::]

    idx = max_samples-1
    while ((np.abs(i[idx] - i[0]) > 0.5) or (np.abs(q[idx] - q[0]) > 0.5) ): 
        idx = idx - 1


    i = i[0:idx:]
    q = q[0:idx:]

    return [i, q]


outputfile = 'tx_qpsk_30mbd_seq_'

num_symbols = 1000
F_baud = 30720000 
F_sample = 491520000
N_pts = 30720
Amp = 30000

sps = F_sample // F_baud # samples per symbol

syms_qpsk = np.array([ 1. + 1.j, -1. + 1.j, -1. - 1.j, 1. - 1.j ])
#bits = np.random.randint(0, 4, num_symbols) # Our data to be transmitted, 1's and 0's
bits = np.zeros(num_symbols, dtype=int)

seq = np.zeros(4, dtype=int)
for i in range(4):
    seq[i] = int(sys.argv[i+1])

for k  in range(num_symbols):
    bits[k] = seq[k % 4]

I = np.array([])
Q = np.array([])

for bit in bits:
    pulseI = np.zeros(sps)
    pulseI[0] = np.real(syms_qpsk[bit]) # set the first value to either a 1 or -1
    I = np.concatenate((I, pulseI)) # add the 8 samples to the signal
    pulseQ = np.zeros(sps)
    pulseQ[0] = np.imag(syms_qpsk[bit]) # set the first value to either a 1 or -1
    Q = np.concatenate((Q, pulseQ)) # add the 8 samples to the signal


# Create our raised-cosine filter
num_taps = 101
beta = 0.35
Ts = 1/F_baud # Assume sample rate is 1 Hz, so sample period is 1, so *symbol* period is 8
t = np.arange(-51/F_sample, 52/F_sample, 1/F_sample) # remember it's not inclusive of final number

h = np.sinc(t/Ts) * np.cos(np.pi*beta*t/Ts) / (1 - (2*beta*t/Ts)**2)



# Filter our signal, in order to apply the pulse shaping
I_shaped = np.convolve(I, h)


"""
for i in range(num_symbols):
    x = [i*sps+num_taps//2+1,i*sps+num_taps//2+1]
    y = [min(I_shaped), max(I_shaped)]
    plt.plot(x, y)
"""


Q_shaped = np.convolve(Q, h)



"""
for i in range(num_symbols):
    #I_tot += [i*sps+num_taps//2+1,i*sps+num_taps//2+1]
    plt.plot([i*sps+num_taps//2+1,i*sps+num_taps//2+1], [min(Q_shaped), max(Q_shaped)])
"""




i = I_shaped[0:N_pts]
q = Q_shaped[0:N_pts]
amp_max = max(max(i), max(q))

i = i * (Amp/amp_max)
q = q * (Amp/amp_max)

[i, q] = trim_signal(4096, i, q)
blen = len(i)
[i, q] = replicate(122880, i, q)
tlen = len(i)

if plot:
    plt.plot(i)
    plt.plot(q)
    plt.show()
    plt.plot(i[::sps], q[::sps], '.')
    plt.show()

iq = np.vstack((i, q)).ravel('F')

dt = np.dtype('<i2')  
fname = outputfile+ str(seq[0])+str(seq[1])+str(seq[2])+str(seq[3])+'-'+str(blen*4)+'-'+str(tlen*4)+'-.bin'
iq.astype(dtype=dt).tofile(fname)
toks = fname.split('-')
print(toks)


"""
S = np.fft.fftshift(np.fft.fft(I_shaped))
S_mag = np.abs(S)
S_phase = np.angle(S)
plt.figure(2)
plt.plot(S_mag)
plt.grid(True)
plt.show() 
"""




