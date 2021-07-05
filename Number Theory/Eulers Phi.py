# SieveOfDivisors, Build in O(NlogN)
# Query Phi(n) in O(1) if n <= mxN else on O(sqrt(n))
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
# Starts from here...
mxN = 10 ** 6    
isp = []
prime = []
phi = []
def Sieve():
    global isp
    global prime
    for i in range(0 , mxN):
        isp.append(0)
    isp[0] = isp[1] = 1
    for i in range(4 , mxN , 2):
        isp[i] = 1
    sq = int(math.sqrt(mxN)) + 1
    for i in range(3 , sq , 2):
        if (isp[i] == 0):
            for j in range(i * i , mxN, i + i):
                isp[j] = 1
    prime.append(2)
    for i in range(3 , mxN , 2):
        if (isp[i] == 0):
            prime.append(i)
    return 0
def SieveOfEulersPhi():
    global phi
    for i in range(0 , mxN):
        phi.append(0)
    phi[1] = 1
    for i in range(2 , mxN):
        if (phi[i] == 0):
            phi[i] = i - 1
            for j in range(i + i, mxN, i):
                if (phi[j] == 0):
                    phi[j] = j
                phi[j] -= phi[j] // i
def Phi(n):
    if (n < mxN): return phi[n]
    ans = n
    for i in range(0 , len(prime)):
        x = prime[i]
        if (x * x > n): break
        if (n < mxN and isp[n] == 0): break
        if (n % x == 0):
            while (n % x == 0):
                n //= x
            ans -= ans // x
    if (n != 1):
        ans -= ans // n
    return ans
# End here
def main():
    Sieve()
    SieveOfEulersPhi();
    n = int(input())
    print(Phi(n))
main()
