import numpy as np 
import matplotlib.pylab as plt 

Er, Ei = np.loadtxt('Spectrum_ECS.dat', unpack=True)

plt.scatter(Er,Ei)
plt.show()