import matplotlib.pyplot as plt
from matplotlib import style

slices=[7,2,2,13]

activity=['sleep','eat','work','play']
cols=['c','m','g','y']

plt.pie(slices,
        labels=activity,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0.1,0.1,0.1,0),
        autopct='%.1f%%')  # Exlode() to pull out slice
                            # %.3 means 3 till decimal point
                            # startangle=90 means slicing start from 90 angle
plt.title('Pie plot')

plt.show()
