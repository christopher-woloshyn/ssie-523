import matplotlib
matplotlib.use('TkAgg')
from pylab import *

import json
import networkx as nx

def initialize():
    global g, pos
    with open('starwars-episode-4-interactions-allCharacters.json') as f:
        data = f.read()
    raw_data = json.loads(data)
    g = nx.Graph()
    names = raw_data['nodes']
    for link in raw_data['links']:
        g.add_edge(names[link['source']]['name'],
                   names[link['target']]['name'],
                   weight=link['value'])
    pos = nx.spring_layout(g)

def observe():
    global g, pos
    cla()
    nx.draw(g, pos=pos, with_labels=True)

def update():
    global g, pos
    i = choice(g.nodes)
    nbs = list(g.neighbors(i))
    nbs2 = []
    for j in nbs:
        nbs2 += list(g.neighbors(j))
    nbs2 = list(set(nbs2).difference(nbs + [i]))
    if len(nbs2) > 0:
        g.add_edge(i, choice(nbs2))
    if len(nbs) > 0:
        g.remove_edge(i, choice(nbs))
    pos = nx.spring_layout( g, pos = pos, iterations=2, k=1)

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
