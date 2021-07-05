import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mxN = 100000
isp = []
prime = []
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
def Phi(n):
    if n < 0: 
        n *= -1
    res = n
    tot_prime = len(prime)
    for i in range(0 , tot_prime):
        x = prime[i]
        if x * x > n: break
        if (n % x == 0):
            while (n % x == 0):
                n //= x
            res -= res // x
    if n != 1:
        res -= res // n
    return res
def main():
    Sieve()
    while (1):
        n = int(input())
        if n == 0: break
        sys.stdout.write(str(Phi(n)) + "\n")
main()
