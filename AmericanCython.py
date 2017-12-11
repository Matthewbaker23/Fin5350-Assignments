#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:56:24 2017

@author: mattbaker
"""
#American Call Option In Cython
cdef class PricingEngine:
    """A base class for option pricing engines."""
    cdef double calculate(self, Option option, MarketData data):
        pass

cdef class BinomialEngine(PricingEngine):
    """An interface class for binomial pricing engines."""
    def __init__(self, nsteps):
        self._nsteps = nsteps

    cdef double calculate(self, Option option, MarketData data):
        pass


cdef class AmericanBinomialEngine(BinomialEngine):
    """A concrete class for the European binomial option pricing model."""

    cdef double calculate(self, Option option, MarketData data):
        cdef double expiry = option.expiry
        cdef double strike = option.strike
        cdef double spot = data.spot
        cdef double rate = data.rate
        cdef double vol = data.vol
        cdef double div = data.div
        cdef double dt = expiry / self._nsteps
        cdef double u = cexp(((rate - div) * dt) + vol * csqrt(dt))
        cdef double d = cexp(((rate - div) * dt) - vol * csqrt(dt))
        cdef double pu = (cexp((rate - div) * dt) - d) / (u - d)
        cdef double pd = 1.0 - pu
        cdef double df = cexp(-rate * expiry)
        cdef double spot_t = 0.0
        cdef double payoff_t = 0.0
        cdef unsigned long nodes = self._nsteps + 1
        cdef unsigned long i

        for i in range(nodes):
        St[i] = S * (u **(steps - i)) * (d ** i)
        Ct[i] = option.value(St[i])
        
    for i in range((steps - 1), -1, -1):
        for j in range(i+1):
            Ct[j] = dpu * Ct[j] + dpd * Ct[j+1]
            St[j] = St[j] / u
            Ct[j] = np.maximum(Ct[j], option.value(St[j]))

    return Ct[0] 