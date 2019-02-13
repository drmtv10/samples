#!/bin/python
# monte-carle simulation of coin-toss

from random import random

def head():
    if random() >= 0.5:
        return True
    else:
        return False

def coin_toss(times):
    """
    toss coin and return number of times head
    input - times : number of times coin-toss should be done
    output - count : number of times head is the outcome of coin-toss
    """
    heads = 0
    for _ in range(times):
        if head():
            heads += 1
    return heads

def record_cointoss():
    ct=list()
    for _ in range(1000):
        ct.append(coin_toss(32))

    print ct
    
    for i in ct:
        print (str('*')*int(i/10))

if __name__ == '__main__':
    record_cointoss()
    
    
