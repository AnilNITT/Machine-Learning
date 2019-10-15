import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(211)  # 211 means vertical 2 plot , horizental 1 plot, 1st plot bcoz multiple plots so
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212) # 212 means  2 vertical plot, 1 horoizental plot, this is 2nd plot bcoz we have multiple plots so
plt.plot(t2,np.cos(2*np.pi*t2),'g')

plt.show()
