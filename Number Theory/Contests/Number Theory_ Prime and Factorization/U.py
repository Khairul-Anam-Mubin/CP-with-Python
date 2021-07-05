# Problem Link: https://vjudge.net/contest/444859#problem/U
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
    
def main():
    mxN = 1000001
    isp = []
    prime = []
    for i in range(0 , mxN):
        isp.append(0)
    for i in range(4 , mxN , 2):
        isp[i] = 1
    sq = int(math.sqrt(mxN)) + 1
    for i in range(3 , sq , 2):
        if isp[i] == 0:
            for j in range(i * i , mxN , i + i):
                isp[j] = 1
    prime.append(2)
    for i in range(3 , mxN , 2):
        if isp[i] == 0:
            prime.append(i)
    nod = []
    for i in range(0 , mxN):
        nod.append(0)
    for i in range(1 , mxN):
        for j in range(i , mxN, i):
            nod[j] += 1
    ans = []
    for i in range(1 , mxN):
        n = nod[i]
        pf = []
        for j in range(0 , len(prime)):
            x = prime[j]
            if x * x > n:
                break
            while n % x == 0:
                n //= x
                pf.append(x)
        if n != 1: 
            pf.append(n)
        if len(pf) == 2:
            if pf[0] != pf[1]:
                ans.append(i)
    for i in range(8 , len(ans), 9):
        sys.stdout.write(str(ans[i]) + "\n")
main()
