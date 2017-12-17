#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:01:36 2017

@author: mattbaker
"""

print("I'm going to guess your number between 1 and 100, if my guess is correct, type 'Correct'")
print("If my guess is too high type 'High'")
print("If it's less than, press 'Low'")

lowerbound = 0
upperbound = 100
number = int((upperbound + lowerbound)/2)
done = False
tries = 0
guess = input(number)

while done !=True:
    if guess == "High":
        upperbound = number
        number = int((upperbound + lowerbound)/2)
        guess = input(number)
    elif guess == "Low":
        lowerbound = number
        number = int((upperbound + lowerbound)/2)
        guess = input(number)
    elif guess == "Correct":
        print("I got it! And in only ", tries, "tries")
        done = True 
    tries += 1
print("See, the house always!!")

50
60