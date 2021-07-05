#problem link: https://vjudge.net/contest/444859#problem/N
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mxN = 101
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
def NumOfDigit(n):
    cnt = 0
    while (n):
        n //= 10
        cnt += 1
    return cnt
def ShiftPrint(n):
    digits = NumOfDigit(n)
    x = 3 - digits
    s = ""
    while (x):
        s += " "
        x -= 1
    s += str(n)
    return s
def main():
    Sieve()
    #print(prime)
    while (1):
        n = int(input())
        if (n == 0): break
        v = []
        for i in range(0 , mxN):
            v.append(0)
        for i in range(0 , len(prime)):
            if (prime[i] > n): break
            x = n
            cnt = 0
            while (x // prime[i]):
                cnt += x // prime[i]
                x //= prime[i]
            v[prime[i]] = cnt
        sys.stdout.write(ShiftPrint(n) + "! =")
        cnt = 1
        for i in range(0 , len(prime)):
            if prime[i] > n: break
            if (cnt == 16):
                sys.stdout.write("\n      " + ShiftPrint(v[prime[i]]))
            else:
                sys.stdout.write(ShiftPrint(v[prime[i]]))
            cnt += 1
        sys.stdout.write("\n")
main()
