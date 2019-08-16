from pylab import *
# Two variable example from lecture
"""
x = 1.
y = 1.

def f(x, y):
    nx =  0.5*x + 0.8*y
    ny = -0.5*x + 1*y
    return nx, ny

xresult = [x]
yresult = [y]
for t in range(100):
    x, y = f(x, y)
    xresult.append(x)
    yresult.append(y)
plot(xresult)
plot(yresult)
"""
# Non-linear example from lecture
"""
a0, k = 3.7, 20.
x = 0.001 
def a(x):
    return(1-a0)/k*x + a0
def f(x):
    return a(x)*x
result = [x]
for t in range(200):
    x = f(x)
    result.append(x)
plot(result)
"""
# Fibonacci sequence; Exercise 4.8
x = 1.
y = 1.

def f(x, y):
    nx = x + y
    ny = x
    return nx, ny

result = [x, y]
for i in range(10):
    x, y = f(x, y)
    result.append(x)
print(result)
plot(result)