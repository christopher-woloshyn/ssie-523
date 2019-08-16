from pylab import *
from sympy import *

from sympy.abc import X, Y, p

X = binomial(8, 3)*p**3*(1-p)**5
Y = X + binomial(8, 2)*p**2*(1-p)**6

plot(X*(1-p)+Y*p, p, (p, 0, 1))
