import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx
import meme

def initialize():
    global n, memes, memes2, main_graph, pos

    meme.Meme.id = 0
    n = 4 # Number of original memes.

    memes = [meme.Meme() for i in range(n)]
    memes2 = memes

    main_graph = nx.Graph()
    pos = nx.spring_layout(main_graph)

def observe():
    global n, memes, memes2, main_graph, pos

    cla() # to clear the visualization space.

    for m in memes:
        main_graph.add_node(m.id)

        for j in m.children:
            main_graph.add_edge(m.id, j.id)

    pos = nx.spring_layout(main_graph)
    nx.draw(main_graph, pos=pos, with_labels=True,
            node_size=[i.popularity*2000 if i.alive else 200 for i in memes],
            node_color=['red' if i.alive else 'orange' for i in memes])

def update():
    global n, memes, memes2, main_graph, pos

    m = choice(memes) # stochastic updating.

    if random() < 0.05: # 5% chance that an original memes joins the system.
        memes2.append(meme.Meme())

    if not m.alive: # skips running methods if the chosen meme is dead.
        return

    m.getOlder()
    m.die()
    child = m.reproduce()

    if child:
        memes2.append(child)

    memes, memes2 = memes2, memes

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
