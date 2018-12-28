#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 28 28

@author: cpmcintyre
"""

## Function to simulate roulette wheel and betting strategy

import random

bankroll = 100
stake = 1
count = 0
while bankroll>0:
    if random.uniform(0,1)<= .486:
        bankroll += stake
        stake = 1
    else:
        bankroll -= stake
        stake = 2*stake
    count +=1 

print(count) 




#####
##### 
#####running the simulation on different sizes of initial stakes

br = [10,100,1000,10000,10000,1000000,1000000000]

def gamble(money, probability, stk):
    stake = stk
    count = 0
    br = money
    while money>0:
        if random.uniform(0,1)<= probability:
            br += stake
            stake = 1
        else:
            money -= stake
            stake = 2*stake
        count +=1 
    print(count)
    
for i in br:
    gamble(i, .486, 1)