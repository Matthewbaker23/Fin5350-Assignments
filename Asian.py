#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:52:06 2017

@author: mattbaker
"""
#NOTES 12/4
##CONTROL VARIATE NOTES
import numpy as np
def f(x):
    value = 1/ (1+x)
    return value
def g(x):
    value = 1 + x
    return value
truth = 3.0/2.0
truth 
##The Naive Solution
n = 1500
u = np.random.uniform()
x1 = f(u)
x1.mean()
x1.var()
x1.std()
se = x1.std()/ np.sqrt(n) #Standard Error
se
##The Control Variate Solution
c = 0.4773 #This is Beta in A*=Abar+Beta(Gbar-G)
y = g(u)
x2 = f(u) + c * (g(u) - truth)
x2.mean()
se2= x2.std()/np.sqrt(n) #Standard Error
se2


##NAIVE MONTE CARLO METHOD IN A BLACK SCHOLES WORLD
def VanillaCallPayoff(spot, strike):
    return np.maximum(spot-strike, 0)
#Def the Option
S = 100
K = 100 
r = 0.06
v = .2
q = 0
T = 1

dt = T
nudt = (r - q - .5 * v * v) * dt
sigdt = v * np.sqrt(dt)

#Vectorized Path
M = 100000
z = np.random.normal(size=M)
z = np.concatenate(z, -z)
spot_t = S * np.exp(nudt + sigdt * z)
call_t= VanillaCallPayoff(spot_t, K)

call_price = np.exp(-r*T) * call_t.mean()
call_price

se = call_t.std()/np.sqrt(M)
se

print("The Naive Monte Carlo Price is: {0:.3f}". format(call_price))
print("The Naive Monte Carlo StdErr is: {0:.3f}". format(se))


##CONTROL VARIATE METHOD
def VanillaCallPayoff(spot, strike):
    return np.maximum(spot-strike, 0)
#Def the Option
S = 100
K = 100
r = 0.06
v = .2
q = 0
T = 1
M = 10000 #Number of MC replications
N = 10 #Number of MC steps in a particular path

dt = T
nudt = (r - q - .5 * v * v) * dt
sigdt = v * np.sqrt(dt)


spot_t = np.empty((N))
call_t  = np.empty(M)

z = np.random.normal(size=(M,N))

for i in range(M):
   
    spot_t[0] = S
    for j in range(1,N):
        spot_t[j] = S * np.exp(nudt + sigdt * z[i, j])
    call_t = VanillaCallPayoff(spot_t, K)

call_price = np.exp(-r*T) * call_t.mean()
call_price

se = call_t.std()/np.sqrt(M)
se

print("The Naive Monte Carlo Price is: {0:.3f}". format(call_price))
print("The Naive Monte Carlo StdErr is: {0:.3f}". format(se))


##THE CONTROL VARIATE APPROACH IN A BS WORLD
#We will use the BS Delta formula for our Control Variate. 
#We can write the BS Delta from
import scipy as sp

def BlackScholesDelta(spot_t[j], t, K, T, v, r, q):
    tau = T - t
    d1 = (np.log(spot_t[j]/K) + (r - q + 0.5 * v * v) * tau) / (v * np.sqrt(tau))
    delta = np.exp(-q * tau) * norm.cdf(d1) 
    return delta

erddt = np.exp((r - q) * dt)    
beta = -1.0

spot_t = np.empty((N))
call_t  = np.empty(M)
z = np.random.normal(size=(M,N))

for i in range(M):
        #spot_t = spot
        convar = 0.0
        #z = np.random.normal(size=int(engine.time_steps))
        spot_t[0]= S
        
        for j in range(1, N):
            t = i * dt
            delta = BlackScholesDelta(spot_t[j], t, K, T, v, r, q)
            spot_t[j] = spot_t[j-1] * np.exp(nudt + sigdt * z[i])
            convar+= delta * (spot_t[j] - spot_t[j-1] * erddt)
            #spot_t = spot_tn

        call_t[i] = VanillaCallPayoff(spot_t[-1], K) + beta * convar
        
disc = np.exp(-r * T)
call_prc = disc * call_t.mean()
call_prc

##CONTROL VARIATE FOR ARITHMETIC ASIAN
a = np.log(G[t])+ ((N-M)/N) * (np.log(S)+v(t[M+1]-t)+.5*v*(T-t[m+1])
b = ((N-M)*(N-M)/N*N)*v*v*(t[M+1]-t)+(v*v*(T-t[m+1]))/(6*N*N)*(N-M)(2(N-M)-1)
v = M - delta - .5*v*v
x = (a - np.log(K) + b)/np.srt(b)


