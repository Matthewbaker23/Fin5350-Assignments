#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:03:39 2017

@author: mattbaker
"""
import scipy as sp
import numpy as np

S = 41.0
K = 40.0
r = 0.08
v = 0.3
T = 1.0
steps = 3
numsims = 10000
dt = T/steps
call = sp.zeros([numsims], dtype=float)
for j in range(0, numsims):
    St=S
    total=0
    for i range(0, int(numsteps)):
        e=sp.random.normal()
        ST*=sp.exp((r-0.5*v*v)*dt+v*e*sp.sqrt(dt))
        total+=St
    price_average=total/numsteps
    call[j]=max(price_average-K,0)
call_price= sp.mean(call)*sp.exp(-r*T)
call_price
##ASIAN OPTION
def AsianPayoff(path, strike):
    spot_t = path.mean()
    return np.mean(spot_t - strike, 0.0)
    
#Simulating Paths
reps = 3
steps = 3
path = np.zeros((reps, steps))

dt= T / steps
nudt = (r - q - 0.5 * v * v) * dt
sigdt = v * np.sqrt(dt)

path 
path[:,0] = S
path

##For every row on the zeroth column; set the value to S.
for i in range (reps):
    z = np.random.normal(size=steps)
    for j in range(1, steps):
        path[i, j] = path[i, j-1] * np.exp(nudt + sigdt * z[j])
path 

#These create a table where the Stock Price is the column and the time stamp is the row.
#For the Asian Option we would want to average the Stock Prices in each row. 

#NOTES ON ARITHMETIC ASIAN (12/4)
#CONTROL VARIATE SAMPLING

