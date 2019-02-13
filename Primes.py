#!/bin/python
# Intro to generator / generator expresssion in python
# This has a run time of O(N * (N^0.5)) or O(N^3/2).
# Better run time of O(N^1/2 * logN) can be achieved
# with Sieve of Eratosthenes algorithm, which adds O(N)
# space requirement for array used

def check_prime(num):
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

def Primes(N):
    number = 1
    while number < N:
        number += 1
        if check_prime(number):
            yield number

if __name__ == '__main__':
    N = raw_input('enter number:')
    print 'Primes less than {} are calculated:'.format(N)
    for x in Primes(int(N)):
        print x
    
    
