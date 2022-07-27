import pyworld as pw
import numpy as np
from levinson_durbin import autocorr, LevinsonDurbin

if __name__ == "__main__":
  lpcOrder = 32
  s = np.zeros(2048)
  r = autocorr(s, lpcOrder+1)
  a, e = LevinsonDurbin(r, lpcOrder)
  
  
