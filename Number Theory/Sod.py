# Sum of Divisors, Build in O(NlogN)
# Query sod(n) in O(1) if n <= mxN else on O(sqrt(n))
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
# Starts from here...
mxN = 10 ** 6    
isp = []
prime = []
sod = []
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
def SieveOfDivisors():
    global sod
    for i in range(0 , mxN):
        sod.append(0)
    for i in range(1 , mxN):
        for j in range(i , mxN , i):
            sod[j] += i
def Sod(n):
    if (n < mxN): return sod[n]
    ans = 1
    for i in range(0 , len(prime)):
        x = prime[i]
        if (x * x > n): break
        if (n < mxN and isp[n] == 0): break
        if (n % x == 0):
            tmpsum = 1
            p = 1
            while (n % x == 0):
                p *= x
                tmpsum += p
                n //= x
            ans *= tmpsum
    if (n != 1):
        ans *= (n + 1)
    return ans
# End here
def main():
    Sieve()
    SieveOfDivisors();
    n = int(input())
    print(Sod(n))
main()
