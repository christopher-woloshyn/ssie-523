from pylab import *
from mpl_toolkits.mplot3d import Axes3D

xvalues, yvalues = meshgrid(arange(-5, 5.5, 0.05), arange(-5, 5.5, 0.05))
zvalues = sin(xvalues*yvalues)

ax = gca(projection='3d')

ax.plot_surface(xvalues, yvalues, zvalues)

show()
