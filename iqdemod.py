import scipy as sp
import scipy.signal as sig
import matplotlib.pylab as plt
import numpy as np
import sys, getopt

def LPF(signal, fc, Fs):
    """Low pass filter, Butterworth approximation.

    Parameters
    ----------
    signal : 1D array of floats
        Signal to be filtered.
    fc : float
        Cutt-off frequency.
    Fs : float
        Sampling frequency.

    Returns
    -------
    signal_filt : 1D array of floats
        Filtered signal.
    W : 1D array of floats
        The frequencies at which 'h' was computed, in Hz. 
    h : complex
        The frequency response.
    """
    o = 5  # order of the filter
    fc = np.array([fc])
    wn = 2*fc/Fs

    [b, a] = sig.butter(o, wn, btype='lowpass')
    [W, h] = sig.freqz(b, a, worN=1024)

    W = Fs*W/(2*np.pi)

    signal_filt = sig.lfilter(b, a, signal)
    return(signal_filt, W, h)



CarrierTxPhaseErr = 0.0
CarrierTxFreq = 1000000

CarrierRxPhaseErr = 0.0
CarrierRxFreq = 1000000

f = 1000

t = np.linspace(0, 0.1, 2000000)

i_off = 0
q_off = 0
iq_ph_err = 0
amp_err = 1
iq_freq_err = 1

it = np.sin(2*np.pi*f*t) + i_off
qt = amp_err*np.sin(2*np.pi*f*iq_freq_err*t + iq_ph_err) + q_off

s = np.multiply(it, np.cos(2*np.pi*CarrierTxFreq*t)) + np.multiply(qt, np.sin(2*np.pi*CarrierTxFreq*t + CarrierTxPhaseErr))


ir = np.multiply(s, np.cos(2*np.pi*CarrierRxFreq*t+np.pi/8))
qr = np.multiply(s, np.sin(2*np.pi*CarrierRxFreq*t+CarrierRxPhaseErr+np.pi/8))

[irf, W, h]  = LPF(ir, 10000, 2000000)
[qrf, W, h]  = LPF(qr, 10000, 2000000)

plt.plot(it, '.-')
plt.plot(irf, '.-')

plt.show()

plt.plot(qt, '.-')
plt.plot(qrf, '.-')

plt.show()
