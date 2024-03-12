import numpy as np
import matplotlib.pyplot as plt



h11 = 1.5  
h = 10.0
h22 = h - h11
a2 = -0.7 
a3 = -0.7  
f = 2500  
f = f * 1e6 
dmin = 10.0 
dmax = 50.0  
lp = 1000 

c = 3e8  

zakres = dmax - dmin
d = np.linspace(dmin, dmax, lp)
d1 = d
d2 = 2 * np.sqrt(h22**2 + (d**2) / 4)
d3 = 2 * np.sqrt(h11**2 + (d**2) / 4)
fi1 = -2 * np.pi * f * d1 / c
fi2 = -2 * np.pi * f * d2 / c
fi3 = -2 * np.pi * f * d3 / c


PrP0 = np.abs(1 / d1 * np.exp(1j * fi1) +
              a2 / d2 * np.exp(1j * fi2) +
              a3 / d3 * np.exp(1j * fi3))

PrP0_dB = 20 * np.log10(PrP0)


plt.figure(figsize=(10, 6))
plt.plot(d, PrP0_dB)
plt.title('Relative power decay of radio signal as a function of distance')
plt.xlabel('Distance between antennas [m]')
plt.ylabel('Power decay [dB]')
plt.grid(True)
plt.show()

