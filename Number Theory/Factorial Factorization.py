# Sieve, Build in O(NloglogN)
# Generating Factorization in O(NlogN)
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
# Starts from here...
mxN = 10 ** 6    
isp = []
prime = []
FF = []
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
def FactorialFactorization(n):
    global FF
    FF = []
    for i in range(0 , len(prime)):
        if prime[i] > n: break
        x = n
        freq = 0
        while (x // prime[i]):
            freq += x // prime[i]
            x //= prime[i]
        FF.append([prime[i] , freq])
# End here
def main():
    Sieve()
    n = int(input())
    FactorialFactorization(n)
    print(FF)
main()
