from pylab import *
import networkx as nx

def f(x):
    if x % 2 == 1:
        return 3*x + 1
    else:
        return x // 2

def main():
    g = nx.DiGraph()
    
    for x in range(1, 33):
        while x > 1:
            g.add_edge(x, f(x))
            x = f(x)
    
    ccs = [cc for cc in nx.connected_components(g.to_undirected())]
    n = len(ccs)
    w = ceil(sqrt(n))
    h = ceil(n / w)
    
    for i in range(n):
        subplot(h, w, i+1)
        nx.draw(nx.subgraph(g, ccs[i]), with_labels = True)
        
    show()
    
main()