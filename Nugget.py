#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:12:58 2017

@author: mattbaker
"""

def nuggetnum(candidate):
        for a in range(0, candidate//6+1):
            for b in range(0, candidate//9+1):
                for c in range(0, candidate//20+1):
                    if 6*a + 9*a + 20*c == candidate:
                        return True
    return False

def main():
        success = 0
        biggest = 0
        candidate = 6
        while success != 6:
            if(nuggetnum(candidate)):
                success += 1
            else:
            success = 0
            biggest = candidate 
        candidate += 1

print("The highest number of nuggets you cannot buy is", biggest,)
    