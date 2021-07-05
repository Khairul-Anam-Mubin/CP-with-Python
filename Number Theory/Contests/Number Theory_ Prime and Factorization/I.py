# Problem Link: https://vjudge.net/contest/444859#problem/I
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mxN = 100000
isp = []
prime = []
def Sieve():
    for i in range(0 , mxN + 1, 1):
        isp.append(1)
    isp[0] = isp[1] = 0
    for i in range(4 , mxN + 1, 2):
        isp[i] = 0
    sq = int(math.sqrt(mxN)) + 1
    for i in range(3 , sq , 2):
        if isp[i] == 1:
            for j in range(i * i , mxN + 1, i + i):
                isp[j] = 0
    prime.append(2)
    for i in range(3 , mxN + 1 , 2):
        if isp[i] == 1:
            prime.append(i)
def IsPrime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    if n < mxN:
        return isp[n]
    sq = int(math.sqrt(n)) + 1
    for i in range(0 , len(prime)):
        if prime[i] > sq:
            return 1
        if n % prime[i] == 0:
            return 0
    return 1    
def main():
    Sieve()
    t = int(input())
    for tc in range(t):
        n = int(input())
        dec = -1
        if n > 5:
            if n % 2 == 1: 
                n -= 2
                dec = -2
            else:
                n -= 1
                dec = -2
        else:
            n -= 1
        for i in range(n, 1, dec):
            if IsPrime(i):
                sys.stdout.write(str(i) + "\n")
                break
main()
