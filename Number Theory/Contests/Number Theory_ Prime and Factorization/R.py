#problem link : https://vjudge.net/contest/444859#problem/R
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mxN = 1000001
isp = []
prime = []
pf_list = []
def Sieve():
    global isp
    global prime
    for i in range(0 , mxN):
        isp.append(0)
    for i in range(4 , mxN, 2):
        isp[i] = 1
    for i in range(3 , mxN, 2):
        if (isp[i] == 0):
            for j in range(i * i, mxN, i + i):
                isp[j] = 1
    prime.append(2)
    for i in range(3 , mxN , 2):
        if (isp[i] == 0):
            prime.append(i)
def PrimeFactorization(n):
    global pf_list
    pf_list = []
    for i in range(len(prime)):
        x = prime[i]
        if (x * x > n): break
        while (n % x == 0):
            n //= x
            pf_list.append(x)
    if (n != 1):
        pf_list.append(n)
def main():
    Sieve()
    while (1):
        n = int(input())
        if (n < 0): break
        PrimeFactorization(n)
        for i in range(0 , len(pf_list)):
            sys.stdout.write("    " + str(pf_list[i]) + "\n")
        sys.stdout.write("\n")
main()
