from pylab import *

a = 2
b = 1
c = .5
d = 1
Dt = .001
end = 50

def initialize():
    global x, y, xresult, yresult, t, timesteps
    x = 0.1
    y = 0.1
    xresult = [x]
    yresult = [y]
    t = 0.
    timesteps = [t]

def observe():
    global x, y, xresult, yresult, t, timesteps
    xresult.append(x)
    yresult.append(y)
    timesteps.append(t)
    
def update():
    global x, y, xresult, yresult, t, timesteps
    x = x + a * x * Dt - b * x * y * Dt
    y = y - c * y * Dt + d * x * y * Dt
    t = t + Dt
    
def main():
    initialize()
    while t < end:
        update()
        observe()
    plot(timesteps, xresult, 'b')
    plot(timesteps, yresult, 'r')
    #plot(xresult, yresult, 'black')

main()    