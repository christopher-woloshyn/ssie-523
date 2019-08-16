from pylab import *

def initialize():
    global x, result
    x = 0.1
    result = [x]

def observe():
    global x, result
    result.append(x)

def update():
    global x, result
    x = r*x*(1-x)

def plot_phase_space():
    initialize()
    for t in range(30):
        update()
        observe()
    plot(result)
    ylim(0, 1)
    title('r = ' + str(r))


rs = [2., 2.5, 3, 3.5, 3.8, 4.]
for i in range(len(rs)):
    subplot(2, 3, i + 1)
    r = rs[i]
    plot_phase_space()
show()
