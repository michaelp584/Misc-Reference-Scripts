#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:20:45 2019

@author: michaelpatrick
"""
# Classic Towers of Hanoi solution via recursion. 
def printMove(fr, to):
    print("Move from " + str(fr) + " to " + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1: 
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(2, "P1", "P2", "P3"))