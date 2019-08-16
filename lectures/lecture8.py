import numpy as np
import pylab as pl
"""
A = np.array([[-1, 2], [2, -2]])
eig = np.linalg.eig(A)[0]
eigV = np.linalg.eig(A)[1]

x, y = np.meshgrid(np.arange(0, 3, 0.1), np.arange(0, 3, 0.1))

xv = -x + 2*y
yv = 2*x - 2*y

pl.streamplot(x, y, xv, yv)
pl.plot([0,0.7882], [0, 0.6154], 'r')

#######################
# LATER ON IN LECTURE #
#######################

from sympy import symbols, Matrix

a, b, c, d, x, y = symbols('a b c d x y')

# a, b, c, d > 0

dx = a*x - b*x*y
dy = -c*y + d*x*y

J = Matrix(
        [[dx.diff(x), dx.diff(y)], # column 1
        [dy.diff(x), dy.diff(y)]]) # column 2

J = J.subs({'a':2,
            'b':2,
            'c':1,
            'd':3})

J1 = J.subs({'x':0, 'y':0})
J2 = J.subs({'x':1/3, 'y':1})

eig1 = J1.eigenvals()
eig2 = J2.eigenvals()
"""
#####Note#####
# The eigenvals function returns
# a dictionary where the key
# is the egenvaluse and the value
# is the multiplicity of that
# eigenvalue
##############

# Now we plot the phase space

dt = 0.01
t = 0.
timesteps = [t]
x = 0.1
y = 0.1
xresult = [x]
yresult = [y]

while t < 100:
    # Don't forget Euler Forward Function:
    # x = x + F(x)*dt

    next_x = x + (2*x - 2*x*y)*dt
    next_y = y + (-y + 3*x*y)*dt
    x, y = next_x, next_y
    xresult.append(x)
    yresult.append(y)
    t += dt
    timesteps.append(t)

pl.figure()
pl.plot(xresult, yresult, 'orange')
pl.plot(0,0,'ro')
pl.plot(1/3,1, 'ro')
pl.show()

x, y = np.meshgrid(np.arange(0, 7, 0.1), np.arange(0, 11, 0.1))

xv = 2*x - 2*x*y
yv = -y + 3*x*y

pl.streamplot(x, y, xv, yv)
