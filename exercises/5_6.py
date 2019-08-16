from pylab import *

def initialize():
    global x, xresult
    x = 0.1
    xresult = [x]
    
def observe():
    global x, xresult
    xresult.append(x)

def update():
    global x, xresult
    x = f(x)

def f(x):
    r = 2.5
    k = 1
    return x + r*x*(1 - x/k)

def main():
    initialize()
    t = 20
    for i in range(t):
        update()
        observe()
    plot(xresult, 'b')    
#---------------------------------------------------#
    ### drawing diagonal line
    xmin, xmax = 0, 20
    plot([xmin, xmax], [xmin, xmax], 'k')
    
    ### drawing curve
    rng = arange(xmin, xmax, (xmax - xmin) / 100.)
#---------------------------------------------------#
    plot(rng, map(f, rng), 'k')

    horizontal = [result[0]]
    vertical = [result[0]]
    for i in result[1:]:
        horizontal.append(vertical[-1])
        vertical.append(i)
        horizontal.append(i)
        vertical.append(i)
    plot(horizontal, vertical, 'pink')
    

main()