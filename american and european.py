#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:00:11 2017

@author: mattbaker
"""
#VANILLA OPTION PRICING

##PRICING BACKGROUND INFO
import numpy as np

class VanillaPayoff(object):
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry
    def value(self,spot):
        pass
    
class VanillaCallPayoff(VanillaPayoff):
    def value(self, spot):
        return np.maximum(spot- self.strike, 0.0)
    
class VanillaPutPayoff(VanillaPayoff):
    def value(self, spot):
        return np.maximum(self.strike- spot, 0.0)

S = 41.0
K = 40.0
r = 0.08
v = 0.30
div = 0.0
T = 1.0
N = 3

theCall = VanillaCallPayoff(K, T)
thePut = VanillaPutPayoff(K, T)


###EUROPEAN
from scipy.stats import binom

def EuropeanBinomialPricer(option, S, rate, volatility, dividend, steps):
    nodes = steps + 1
    spotT = 0.0
    callT = 0.0
    dt = option.expiry / steps
    u = np.exp(((rate - dividend) * dt) + volatility * np.sqrt(dt)) 
    d = np.exp(((rate - dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp(r*dt) - d) / (u - d)
    pd = 1 - pu
    
    for i in range(nodes):
        spotT = S * (u ** (steps - i)) * (d ** (i))
        callT += option.value(spotT) * binom.pmf(steps - i, steps, pu)  
    price = callT * np.exp(-r * T)
     
    return price

##PRICE THE CALL
theCall = VanillaCallPayoff(K,T)
callPrice = EuropeanBinomialPricer(theCall, S, r, v, div, N)
callPrice

##PRICE THE PUT
thePut = VanillaPutPayoff(K,T)
putPrice = EuropeanBinomialPricer(thePut, S, r, v, div, N)
putPrice


###AMERICAN
import numpy as np

class VanillaPayoff(object):
    def __init__(self, strike, expiry):
        self.strike = strike
        self.expiry = expiry
    def value(self,spot):
        pass
    
class VanillaCallPayoff(VanillaPayoff):
    def value(self, spot):
        return np.maximum(spot- self.strike, 0.0)
    
class VanillaPutPayoff(VanillaPayoff):
    def value(self, spot):
        return np.maximum(self.strike- spot, 0.0)   

def AmericanBinomialPricer(option, S, rate, volatility, dividend, steps):
    nodes = steps + 1
    dt = option.expiry / steps
    u = np.exp(((rate - dividend) * dt) + volatility * np.sqrt(dt)) 
    d = np.exp(((rate - dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp(r*dt) - d) / (u - d)
    pd = 1 - pu
    disc = np.exp(-rate*dt)
    dpu = disc * pu
    dpd = disc * pd
    
    Ct = np.zeros(nodes)
    St = np.zeros(nodes)
    
    for i in range(nodes):
        St[i] = S * (u **(steps - i)) * (d ** i)
        Ct[i] = option.value(St[i])
        
    for i in range((steps - 1), -1, -1):
        for j in range(i+1):
            Ct[j] = dpu * Ct[j] + dpd * Ct[j+1]
            St[j] = St[j] / u
            Ct[j] = np.maximum(Ct[j], option.value(St[j]))

    return Ct[0]   

S = 41.0
K = 40.0
r = 0.08
v = 0.30
div = 0.0
T = 1.0
N = 3

##PRICE THE CALL AND PUT
CallOption = VanillaCallPayoff(K,T)
Call_Price = AmericanBinomialPricer(CallOption, S, r, v, div, N)
PutOption = VanillaPutPayoff(K,T)
Put_Price = AmericanBinomialPricer(PutOption, S, r, v, div, N)
#Call_Price, Put_Price
print(Call_Price)

:
