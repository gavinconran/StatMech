# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 11:48:36 2016

@author: BESSE Marc
"""


import random, math
import matplotlib.pyplot as plt
import numpy as np

def markov_ND(N, n_trials) :
    
    X = [0.0 for i in range(N)]
    delta = 0.1
    radius_square_old = 0
    n_hits = 0
    for i in range(n_trials):
        print(i)
        k = random.randint(0, N-2)
        x_old_k = X[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        radius_square_new = radius_square_old + x_new_k ** 2 - x_old_k ** 2
        if radius_square_new < 1 :
            radius_square_old = radius_square_new
            X[k] = x_new_k
        t = random.uniform(-1,1)
        if radius_square_new + t**2 < 1.0 : 
            n_hits += 1
            
    res = 2.0 * n_hits / float(n_trials) 
    Q = V_sph(N)/V_sph(N-1)       
    print("Computed value", res)
    print("Theoretical value", Q)
    print("Relative error", abs(res-Q))
    
   
def markov_ND_list(N, n_trials) :
    X = [0.0 for i in range(N)]
    delta = 0.2
    R_sq = []
    radius_square_old = 0
    
    for i in range(n_trials):
        print(i)
        k = random.randint(0, N - 2)
        x_old_k = X[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        radius_square_new = radius_square_old + x_new_k ** 2 - x_old_k ** 2
        if radius_square_new <= 1.0 :
            radius_square_old = radius_square_new
            X[k] = x_new_k
            R_sq.append(np.sqrt(radius_square_new))
            
    hist, bins = np.histogram(R_sq, bins=100)
    
    width = bins[1] - bins[0]
    center = (bins[:-1] + bins[1:]) / 2

    plt.bar(center, hist/(width*n_trials), align='center', width=width)
    plt.xlim(0,1.0)
    x = np.linspace(0,1,100)
    y = [(N-1)*r**(N-2) for r in x]
    plt.plot(x,y, color = 'red')
    plt.title("Normalized histogram")
    plt.show()
    filename = 'Histogram_%.1f.D.png' %N
    plt.savefig(filename)

def markov_ND_Q(N, n_trials) :
    X = [0.0 for i in range(N)]
    delta = 0.1
    n_hits = 0
    radius_square_old = 0
    
    for i in range(n_trials):
        print(i)
        k = random.randint(0, N - 2)
        x_old_k = X[k]
        x_new_k = x_old_k + random.uniform(-delta, delta)
        radius_square_new = radius_square_old + x_new_k ** 2 - x_old_k ** 2
        if radius_square_new < 1 :
            radius_square_old = radius_square_new
            X[k] = x_new_k
        t = random.uniform(-1,1)
        if radius_square_new + t**2 < 1.0 : 
            n_hits += 1
            
    res = 2.0 * n_hits / float(n_trials)  
    Q = V_sph(N)/V_sph(N-1)    
    print(res, Q, abs(res-Q))
            
        
def V_sph(dim) :
    return(math.pi ** (dim / 2.0) / math.gamma(dim / 2.0 + 1.0))
    

def markov_volume(N,n_trials):
    Q = []
    for i in range(2,N+1):
        q,res = markov_ND_Q(i,n_trials)
        Q.append(q)
    V = 2
    for i in range(2,N+1):
        V *= Q[i]
    print(V)
        
        


