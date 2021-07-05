#problem link : https://vjudge.net/contest/444859#problem/Y
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

mxN = 1000001
isp = []
prime = []
nod = []
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
def SieveOfDivisors():
    global nod
    for i in range(0 , mxN):
        nod.append(0)
    for i in range(1 , mxN):
        for j in range(i , mxN , i):
            nod[j] += 1
def Nod(n):
    #if (n <= mxN): return nod[n]
    sq = int(math.sqrt(n)) + 1
    ans = 1
    for i in range(0 , len(prime)):
        x = prime[i]
        if (x * x > n):
            break
        if (n % x == 0):
            cnt = 1
            while (n % x == 0):
                cnt += 1
                n //= x
            ans *= cnt
    if (n != 1):
        ans *= 2
    return ans
def main():
    Sieve()
    #SieveOfDivisors()
    t = int(input())
    for tc in range(1 , t + 1):
        n = int(input())
        ans = Nod(n)
        ans -= 1
        sys.stdout.write("Case " + str(tc) + ": ")
        sys.stdout.write(str(ans) + "\n")
main()
