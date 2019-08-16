import matplotlib
matplotlib.use('TkAgg')
from pylab import *

L = 5000.
k = 100.
n = int(L/k)
Dt = 0.5

def initialize():
    global P, P2, E, E2
    P = zeros([n, n])
    E = zeros([n, n])
    for x in range(n):
        for y in range(n):
            P[x, y] = 0.5 + uniform(-0.1, 0.1)
    P2 = zeros([n, n])
    E2 = zeros([n, n])

def observe():
    global P, E
    subplot(1, 2, 1)
    cla() # to clear the visualization space 1
    imshow(P, vmin = 0)
    title('population')
    subplot(1, 2, 2)
    cla() # to clear the visualization space 2
    imshow(E, vmin = 0)
    title('economy')

Dp, De, a, b, c = 1250, 250, 550, 1., 0.2

def update():
    global P, P2, E, E2
    for x in range(n):
        for y in range(n):
            Pc = P[x, y]       # Neighbors of P
            Pr = P[(x+1)%n, y]
            Pl = P[(x-1)%n, y]
            Pt = P[x, (y+1)%n]
            Pb = P[x, (y-1)%n]

            Ec = E[x, y]       # Neighbors of E
            Er = E[(x+1)%n, y]
            El = E[(x-1)%n, y]
            Et = E[x, (y+1)%n]
            Eb = E[x, (y-1)%n]

            lapP = (Pr + Pl + Pt + Pb - 4*Pc) / (k**2) # Laplacian for P
            lapE = (Er + El + Et + Eb - 4*Ec) / (k**2) # Laplacian for E

            dPdx_dEdx = (Pr-Pl)*(Er-El)/(4*k**2) # Discretized partial derivatives
            dPdy_dEdy = (Pt-Pb)*(Et-Eb)/(4*k**2)

            P2[x, y] = Pc + (Dp*lapP - a*(Pc*lapE + dPdx_dEdx + dPdy_dEdy)) * Dt
            E2[x, y] = Ec + (De*lapE + b*Pc - c*Ec) * Dt

    P, P2, E, E2 = P2, P, E2, E

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
