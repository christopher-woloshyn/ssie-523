import matplotlib
matplotlib.use('TkAgg')
from pylab import *

import json
import networkx as nx

with open('starwars-episode-4-interactions-allCharacters.json') as f:
    data = f.read()
raw_data = json.loads(data)
g = nx.Graph()
names = raw_data['nodes']
for link in raw_data['links']:
    g.add_edge(names[link['source']]['name'],
               names[link['target']]['name'],
               weight=link['value'])

def initialize():
    global g, pos
    for i in g.nodes:
        #g.nodes[i]['choice'] = 0 if random() < 0.9 else 2
        g.nodes[i]['choice'] = 0
    g.nodes['HAN']['choice'] = 1
    rankings = sorted(list(dict(g.degree()).items()), key=lambda x:x[1], reverse=True)
    for i, d in rankings[:5]:
        g.nodes[i]['choice'] = 2 # vaccinate the top 5 most popular people
    pos = nx.spring_layout(g)

def observe():
    global g, pos
    cla()
    nx.draw(g, pos=pos, with_labels = True, vmin = 0, vmax = 2,
           node_color = [g.nodes[i]['choice'] for i in g.nodes])

def update():
    global g, pos
    i = choice(list(g.nodes))
    if g.nodes[i]['choice'] != 0:
        return
    nbs = list(g.neighbors(i))
    x = sum(1 for j in nbs if g.nodes[j]['choice'] == 1)
    r = 0.2 # "Srength" of the product
    if random() < 1 - exp(-r*x**2):
        g.nodes[i]['choice'] = 1

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
