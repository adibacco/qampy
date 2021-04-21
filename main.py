import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

num_symbols = 1000
F_baud = 30720000 
F_sample = 491520000

sps = F_sample // F_baud # samples per symbol

syms_qpsk = np.array([ 1. + 1.j, -1. + 1.j, -1. - 1.j, 1. - 1.j ])
bits = np.random.randint(0, 4, num_symbols) # Our data to be transmitted, 1's and 0's

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
plt.figure(1)
plt.plot(t, h, '.')
plt.grid(True)
plt.show()


# Filter our signal, in order to apply the pulse shaping
I_shaped = np.convolve(I, h)
plt.figure(2)
plt.plot(I_shaped, '.-')
for i in range(num_symbols):
    plt.plot([i*sps+num_taps//2+1,i*sps+num_taps//2+1], [min(I_shaped), max(I_shaped)])

Q_shaped = np.convolve(Q, h)
plt.figure(2)
plt.plot(Q_shaped, '.-')
for i in range(num_symbols):
    plt.plot([i*sps+num_taps//2+1,i*sps+num_taps//2+1], [min(Q_shaped), max(Q_shaped)])
plt.grid(True)
plt.show()


""" S = np.fft.fftshift(np.fft.fft(I_shaped))
S_mag = np.abs(S)
S_phase = np.angle(S)
plt.figure(2)
plt.plot(S_mag)
plt.grid(True)
plt.show() """




