import matplotlib.pyplot as plt
from matplotlib import style

pop_age=[22,55,62,45,21,22,34,42,4,99,102,110,121,122,130,111,115,112,80,75,65,54,44,44,43,42,48]

bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(pop_age,bins,label='pop_age',histtype='bar',color='c',rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Histogram")

#plt.grid(True)

plt.legend()

plt.show()
