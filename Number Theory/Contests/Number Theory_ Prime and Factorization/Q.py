#problem link : https://vjudge.net/contest/444859#problem/Q
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mxN = 1000001
isp = []
prime = []
pf_list = []
tot_pf = 0
def Sieve():
    global isp
    global prime
    for i in range(0 , mxN):
        isp.append(0)
    for i in range(4 , mxN , 2):
        isp[i] = 1
    sq = int(math.sqrt(mxN)) + 1
    for i in range(3 , sq , 2):
        if (isp[i] == 0):
            for j in range(i * i , mxN , i + i):
                isp[j] = 1
    prime.append(2)
    for i in range(3 , mxN):
        if (isp[i] == 0):
            prime.append(i)
def PrimeFactorization(n):
    global pf_list
    global tot_pf
    if n < 0: 
        n *= -1
    tot_pf = 0
    pf_list.clear()
    tot_prime = len(prime)
    i = 0
    while (i < tot_prime):
        if i + 1 < tot_prime:
            x = prime[i]
        elif i + 1 == tot_prime: 
            i = prime[i] - 1
            x = i
            tot_prime = int(math.sqrt(n))
        else:
            x = i
        if x * x > n:
            break
        if n % x == 0:
            while n % x == 0:
                n //= x
            pf_list.append(x)
        i += 1
    if n != 1:
        pf_list.append(n)
    tot_pf = len(pf_list)
    if tot_pf <= 1: return -1    
    return pf_list[tot_pf - 1]
def main():
    Sieve()
    while (1):
        n = int(input())
        if n == 0: break
        #print(PrimeFactorization(n))
        sys.stdout.write(str(PrimeFactorization(n)) + "\n")
main()
    
