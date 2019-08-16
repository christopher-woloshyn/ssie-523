import matplotlib
matplotlib.use('TkAgg')
from pylab import *

class Agent():
    def __init__(self):
        self.is_believer = True if random() < 0.1 else False
    def listen(self, society):
        return choice(society).is_believer
    def consider(self, society):
        if not self.is_believer:
            polls = [self.listen(society) for i in range(5)]
            if polls.count(True) >= 1:
                self.is_believer = True

def initialize():
    global society
    society = [Agent() for i in range(1000)]

def observe():
    global society
    cla() # to clear the visualization space
    hist([1 if a.is_believer else 0 for a in society])

def update():
    global society
    a = choice(society)
    a.consider(society)

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
