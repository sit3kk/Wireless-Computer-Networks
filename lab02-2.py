import numpy as np
import matplotlib.pyplot as plt


h1 = 1.5  
h = 10.0  
h2 = h - h1
a2 = -0.7 
a3 = -0.7  
frequencies_MHz = [2500, 3000, 3500] 
frequencies = np.array(frequencies_MHz) * 1e6 


dmin = 10.0  
dmax = 50.0 
lp = 1000 


Pr = np.zeros((lp, len(frequencies)))  
c = 3e8
lam = c / frequencies
Gr = 1.6
Gt = 1.6


d = np.linspace(dmin, dmax, lp)
d1 = d
d2 = 2 * np.sqrt(h2**2 + (d + h2)**2) / 4
d3 = 2 * np.sqrt(h1**2 + (d + h1)**2) / 4


for i, freq in enumerate(frequencies):
    fi1 = 2 * np.pi * freq * d1 / c
    fi2 = 2 * np.pi * freq * d2 / c
    fi3 = 2 * np.pi * freq * d3 / c


    PrPt = np.abs(1 / d1 * np.exp(-1j * fi1) +
                  a2 / d2 * np.exp(-1j * fi2) +
                  a3 / d3 * np.exp(-1j * fi3))
    PrPt = Gr * Gt * (lam[i] / (4 * np.pi))**2 * PrPt

    Pr[:, i] = PrPt 

maxP = np.max(Pr)

# Convert the power to dB
Pr_dB = 20 * np.log10(Pr / maxP)

# Plot the relative power decay of the transmitted signal as a function of distance
plt.figure(figsize=(10, 6))
for i in range(len(frequencies)):
    plt.plot(d, Pr_dB[:, i], label=f'Frequency {frequencies_MHz[i]} MHz')

plt.title('Relative power decay of radio signal as a function of distance')
plt.xlabel('Distance between antennas [m]')
plt.ylabel('Power decay [dB]')
plt.grid(True)
plt.legend()
plt.show()
