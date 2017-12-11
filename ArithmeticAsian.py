#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:44:22 2017

@author: mattbaker
"""
import numpy as np
import scipy as sp
from scipy.stats.mstats import gmean 
from scipy.stats import norm

##Black Scholes as Control Variate
#Defining the Call Option of a Black Scholes Model
def BlackScholesCall(S, K, r, v, q, tau):
    d1 = (np.log(S/K) + (r - q + 0.5 * v * v) * tau) / (v * np.sqrt(tau))
    d2 = d1 - v * np.sqrt(tau)
    callPrc = (S * np.exp(-q * tau) * norm.cdf(d1)) - (K * np.exp(-r * tau) * norm.cdf(d2))
    return callPrc

def BlackScholesDelta(S, K, r, v, q, tau):
    d1 = (np.log(S/K) + (r - q + 0.5 * v * v) * tau) / v * np.sqrt(tau)
    delta = np.exp(-q * tau) * norm.cdf(d1)
    return delta

S = 100
K = 100
r = 0.06
v = 0.2
q = 0.03
T = 1

BScallPrc = BlackScholesCall(S, K, r, v, q, T)
callDelta = BlackScholesDelta(S, K, r, v, q, T)
print("The BS Call Price is: {0:0.3f}".format(BScallPrc))
print("The BS Call Delta is: {0:0.3f}".format(callDelta))

##Geometric Asian Call
def GeometricAsianCall(S, K, r, v, q, tau, N):
    dt = tau/N
    nu = r - q - 0.5 * v * v
    a = N * (N + 1) * (2.0 * N * 1.0) / 6.0 
    V = np.exp(-r * tau) * S * np.exp(((N+1.0) * nu / 2.0 + v * v * a / (2.0 * N * N)) * dt)
    vavg = v *np.sqrt(a) / (N**(1.5))
    return BlackScholesCall(V, K, r, vavg, 0, tau)
geoPrc = GeometricAsianCall(100, 100, 0.06, .2, 0.03, 1, 10)
print("The Geometric Asian Call is: {0:0.4f}".format(geoPrc))

##Arithmetic Asian Call
def ArithmeticAsianCallPayoff(path, strike):
    spot_t = path.mean()
    return np.maximum(spot_t - strike, 0)

def NaiveAsianPricer(S, K, r, v, q, T, M, N):
    dt = T / N
    nudt= (r - q - .5 * v * v) * dt
    sigdt = v * np.sqrt(dt)
    
    path = np.empty(N)
    
    Ct1 = np.zeros(M)
   
    for i in range(M):
        path[0] = S
        z = np.random.normal(size=N)
        
        for t in range(1, N):
            path[t] = path[t-1] * np.exp(nudt+sigdt *z[t])
        
        Ct1[i] = ArithmeticAsianCallPayoff(path, K)
       
    prc = Ct1.mean()
    prc *= np.exp(-r * T)

    se = Ct1.std() / np.sqrt(M)
    
    return (prc, se)

S = 100
K = 100
r = 0.06
v = 0.2
q = 0.03
T = 1
M = 10000 
N = 10 

arithPrc, arithSe = NaiveAsianPricer(S, K, r, v, q, T, M, N)
arithPrc
print("The Arithmetic Asian Call Price is: {0:0.4f}".format(arithPrc))
print("The Arithmetic Asian Call Standard Error is: {0:0.4f}".format(arithSe))

#Control Variate Pricing
Abar = arithPrc
Gstar = geoPrc
Gbar = BScallPrc

A = Abar + (Gstar - Gbar)
A
print("The Control Variate Price of the Asian Option is: {0:0.4f}".format(A))


