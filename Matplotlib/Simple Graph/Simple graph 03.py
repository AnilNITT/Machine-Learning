from matplotlib import style
# STYLES ARE THERE
# bmh, ggplot, classic, fivethirtyeight, grayscale,
# seaborn-colorblind, seaborn-dark, seaborn-dark-palette,
# seaborn-darkgrid, seaborn-deep, seaborn-muted,
# seaborn-notebook, seaborn-paper, seaborn-pastel,
# seaborn-poster, seaborn-talk, seaborn-ticks,
# seaborn-white, seaborn-whitegrid, seaborn-bright
style.use('dark_background')

x=[5,8,10]
y=[12,16,6]

x1=[6,9,11]
y1=[6,15,7]

plt.plot(x,y)
 # r, c are colors
plt.plot(x,y,'r',label='line one',linewidth=5)
plt.plot(x1,y1,'y',label='line two',linewidth=5)

plt.title("INFO")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.legend()  # corner side label print

plt.grid(True,color='b',linewidth=1)  # grid yellow line

plt.show()
