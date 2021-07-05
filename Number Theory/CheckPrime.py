import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
#starts from here...  
mxN = 10 ** 6    
isp = []
prime = []
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
def IsPrime(n):
    if (n < mxN): return isp[n]
    if (n % 2 == 0): return 1
    sq = int(math.sqrt(n)) + 1
    for i in range(0 , len(prime)):
        x = prime[i]
        if (x * x > n): break
        if (n % x == 0): return 1
    return 0
#end here
def main():
    Sieve()
    n = int(input())
    if (IsPrime(n) == 0):
        sys.stdout.write(str(n) + " is prime\n")
    else: 
        sys.stdout.write(str(n) + " is composite\n")
main()
