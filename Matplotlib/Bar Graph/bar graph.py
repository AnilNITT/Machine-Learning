import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn-dark')

x=[1,3,5,7,9]
y=[5,2,7,8,2]

x1=[2,4,6,8,10]
y1=[8,6,2,5,6]

plt.bar(x,y,label='one',color='y') # color property use there
plt.bar(x1,y1,label='two',color='g')

plt.legend()

plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title("INFO")

plt.grid(True,linewidth=1,color='b')

plt.show()
