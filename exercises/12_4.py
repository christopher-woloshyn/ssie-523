from pylab import *
import networkx as nx

g = nx.DiGraph()

r = 2
L = 9

def config(x):
    return [1 if x & 2**i > 0 else 0 for i in range(L - 1, -1, -1)]

def cf_number(cf):
    return sum(cf[L - 1 - i] * 2**i for i in range(L))

def update(cf):
    nextcf = [0] * L
    for x in range(L):
        count = 0
        for dx in range(-r, r + 1):
            count += cf[(x + dx) % L]
        nextcf[x] = 1 if count > (2 * r + 1) * 0.5 else 0
    return nextcf

piechart = {}
labels = []
values = []

for x in range(2**L):
    val = cf_number(update(config(x)))
    g.add_edge(x, val)
    piechart[str(val)] = piechart[str(val)] + 1 if str(val) in piechart else 1

for i in piechart:
    labels.append(i)
    values.append(piechart[i])

pie(values, labels=labels)

# ccs = [cc for cc in nx.connected_components(g.to_undirected())]
# n = len(ccs)
# w = ceil(sqrt(n))
# h = ceil(n / w)
# for i in range(n):
#     subplot(h, w, i + 1)
#     nx.draw(nx.subgraph(g, ccs[i]), with_labels = True)

show()
