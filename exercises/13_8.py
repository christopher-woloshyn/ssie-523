from pylab import *

xvalues, yvalues = meshgrid(arange(-5, 5.1, 0.1), arange(-5, 5.1, 0.1))

vx = yvalues*cos(xvalues*yvalues)
vy = xvalues*cos(xvalues*yvalues)

streamplot(xvalues, yvalues, vx, vy)

show()
