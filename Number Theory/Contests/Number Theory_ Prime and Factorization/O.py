#problem link : https://vjudge.net/contest/444859#problem/O
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mxN = 100001
isp = []
prime = []
pf_list = []
tot_pf = 0
def Sieve():
    global isp
    global prime
    for i in range(0 , mxN):
        isp.append(0)
    for i in range(4 , mxN , 2):
        isp[i] = 1
    sq = int(math.sqrt(mxN)) + 1
    for i in range(3 , sq , 2):
        if (isp[i] == 0):
            for j in range(i * i , mxN , i + i):
                isp[j] = 1
    prime.append(2)
    for i in range(3 , mxN):
        if (isp[i] == 0):
            prime.append(i)
def PrimeFactorization(n):
    global pf_list
    global tot_pf
    tot_pf = 0
    pf_list.clear()
    tot_prime = len(prime)
    for i in range(0 , tot_prime):
        x = prime[i]
        if x * x > n:
            break
        while n % x == 0:
            n //= x
            pf_list.append(x)
    if n != 1:
        pf_list.append(n)
    tot_pf = len(pf_list)
def main():
    Sieve()
    tc = int(input())
    for i in range(0 , tc):
        n = int(input())
        PrimeFactorization(n)
        lst = []
        x = 1
        for i in range(0 , tot_pf):
            x *= pf_list[i]
            if x >= 10:
                x //= pf_list[i]
                lst.append(x)
                x = pf_list[i]
        lst.append(x)
        lst.sort()
        flag = 1
        for i in lst:
            if i >= 10:
                flag = 0
        if flag == 0:
            lst = [-1]
        for i in lst:
            sys.stdout.write(str(i))
        sys.stdout.write("\n")
main()
