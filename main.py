mport pyworld as pw
import numpy as np
import scipy.signal
from levinson_durbin import autocorr, LevinsonDurbin

lpcOrder = 32
nfft = 2048

def preEmphasis(wave, p=0.97):
  return scipy.signal.lfilter([1.0, -p], 1, wave)

if __name__ == "__main__":
  s = ## write here to load wave file

  s = preEmphasis(s, p)
  s = s * np.hamming(len(s))
  r = autocorr(s, lpcOrder+1)
  a, e = LevinsonDurbin(r, lpcOrder)
  fscale = np.fft.fftfreq(nfft, d = 1.0/ fs)[:nfft/2]

  w, h = scipy.signal.freqz(np.sqrt(e), a, nfft, "whole")
  lpcspec = np.abs(h)
  loglpcspec = 20 * np.log10(lpcspec)

  plot(fscale, loglpcspec[:nfft/2], "r", linewidth=2)
  xlim((0, 10000))
  show() 
