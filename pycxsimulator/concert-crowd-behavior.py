import matplotlib
matplotlib.use('TkAgg')
from pylab import *

L = 100
n = 300

class agent():
    def __init__(self, ID, company=[]):
        self.ID = ID
        self.age = uniform(12, 60)
        self.x, self.y = L/2 + normal(0, 0.1), L + normal(0, 0.1)
        self.company = company
        self.fan = random()
        self.moving = True

    def move(self, crowd):
        if not self.moving:
            return

        # Rule 1: minimize distance to (L/2, 0)
        d1 = array([L/2, 0]) - array([self.x, self.y])
        d1 /= norm(d1) #unit vecot denoting direction forward
        d1 *= self.fan * speed(self.age)

        # Rule 2: Minimize the angle
        d2 = array([L/2, self.y]) - array([self.x, self.y])
        d2 /= norm(d2)
        d2 *= 0.1

        # Rule 3: Avoid collisions
        d3 = array([0, 0], dtype=float)
        for stranger in crowd:
            if stranger != self:
                if norm([stranger.x - self.x, stranger.y - self.y]) < 5*(1 - self.fan):
                    dd = array([self.x, self.y], dtype=float) - array([stranger.x, stranger.y], dtype=float)
                    dd /= 0.3 * norm(dd)
                    d3 += dd

        # Rule 4: Stay with your partner
        p = crowd[self.company[0]]
        d4 = array([p.x, p.y]) - array([self.x, self.y])
        d4 /= norm(d4)

        d = d1 + d2 + d3 + d4

        if norm(d) > speed(self.age):
            d *= speed(self.age)/norm(d)
        self.x += d[0]
        self.y += d[1]
        if self.y < L/4 * (1 - self.fan):
            self.moving = False

def speed(age):
    return -1/800 * (age - 20)**2 + 5

def initialize():
    global crowd
    crowd = [agent(i) for i in range(n)]
    for i in range(0, n, 2):
        crowd[i].company = [i+1]
        crowd[i+1].company = [i]

def observe():
    global crowd
    cla() # to clear the visualization space
    movers = [a for a in crowd if a.moving]
    non_movers = [a for a in crowd if not a.moving]
    if len(movers) > 0:
        plot([a.x for a in movers], [a.y for a in movers], 'ro')
    if len(non_movers) > 0:
        plot([a.x for a in non_movers], [a.y for a in non_movers], 'ko')
    xlim([0, L])
    ylim([0, L])

def update():
    global crowd
    a = choice(crowd)
    a.move(crowd)

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
