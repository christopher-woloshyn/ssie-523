from pylab import *

def P(y, x):
    return y - x

def f(L, C, N):
    if L > 1:
        L, C, N = 1, 0, 0
    if L < 0:
        L = 0
    return L + L*(1 - L)*P(L, C) + L*(1 - L)*P(L, N)

def g(L, C, N):
    if C > 1:
        L, C, N = 0, 1, 0
    if C < 0:
        C = 0
    return C + C*(1 - C)*P(C, L) + C*(1 - C)*P(C, N)

def h(L, C, N):
    if N > 1:
        L, C, N = 0, 0, 1
    if N < 0:
        N = 0
    return N + N*(1 - N)*P(N, L) + N*(1 - N)*P(N, C)

def main():
    
    t = 20
    
    L = .90
    C = .06
    N  = 1 - L - C
    
    L_result = [L]
    C_result = [C]
    N_result = [N]
    for i in range(t):
        tempL = f(L, C, N)
        tempC = g(L, C, N)
        tempN = h(L, C, N)
        
        L, C, N = tempL, tempC, tempN
        
        L_result.append(L)
        C_result.append(C)
        N_result.append(N)
    
    plot(L_result)
    plot(C_result)
    plot(N_result)
        
main()