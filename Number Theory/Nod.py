# Number of Divisors, Build in O(NlogN)
# Query Nod(n) in O(1) if n <= mxN else on O(sqrt(n))
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
# Starts from here...
mxN = 10 ** 6    
isp = []
prime = []
nod = []
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
        nod.append(0)
    for i in range(1 , mxN):
        for j in range(i , mxN , i):
            nod[j] += 1
def Nod(n):
    if (n < mxN): return nod[n]
    ans = 1
    for i in range(0 , len(prime)):
        x = prime[i]
        if (x * x > n): break
        if (n < mxN and isp[n] == 0): break
        if (n % x == 0):
            cnt = 1
            while (n % x == 0):
                n //= x
                cnt += 1
            ans *= cnt
    if (n != 1):
        ans *= 2
    return ans
# End here
def main():
    Sieve()
    SieveOfDivisors();
    n = int(input())
    print(Nod(n))
main()
