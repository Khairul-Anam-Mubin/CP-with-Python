# Problem Link : https://vjudge.net/contest/444859#problem/G
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
def Sieve():
    isp = []
    mxN = 100000
    for i in range(0 , mxN):
        isp.append(0)
    for i in range(4 , mxN , 2):
        isp[i] = 1
    sq = int(math.sqrt(mxN))
    for i in range(3 , sq + 1, 2):
        if isp[i] == 0:
            for j in range(i * i , mxN , i + i):
                isp[j] = 1
    prime = []
    prime.append(2)
    for i in range(3 , mxN , 2):
        if isp[i] == 0:
            prime.append(i)
    return prime
def main():
    prime = Sieve()
    t = int(input())
    for tc in range(t):
        pq = inlist()
        p = pq[0]
        q = pq[1]
        x = 1
        if p < q:
            x = p
        else:
            if p % q != 0:
                x = p
            else:
                x = 1
                for i in prime:
                    if q == 1: break
                    if q % i == 0:
                        tmp = p
                        cnt = 0
                        while q % i == 0:
                            q //= i
                            cnt += 1
                        tot = 0
                        while tmp % i == 0:
                            tmp //= i
                        cnt -= 1
                        while cnt != 0:
                            tmp *= i
                            cnt -= 1
                        x = max(x , tmp)
                if q != 1:
                    while p % q == 0:
                        p //= q
                    x = max(x , p)
        sys.stdout.write(str(x) + "\n")
main()
