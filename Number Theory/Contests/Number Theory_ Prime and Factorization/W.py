#problem link : https://vjudge.net/contest/444859#problem/W
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mod = 10 ** 9 + 7
mxN = 50001
isp = []
prime = []
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
def main():
    Sieve()
    t = int(input())
    for tc in range(1 , t + 1):
        n = int(input())
        sz = len(prime)
        ans = 1
        for i in range(0 , sz):
            if prime[i] > n: break
            cnt = 1
            x = n
            p = prime[i]
            while (x // p):
                cnt += x // p
                x //= p
            ans *= (cnt % mod)
            ans %= mod
        sys.stdout.write(str(ans) + "\n")
main()
