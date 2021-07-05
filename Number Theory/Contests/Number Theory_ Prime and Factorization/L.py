#problem link : https://vjudge.net/contest/444859#problem/L
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
mxN = 100000001
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
    while (1):
        n = int(input())
        if n == 0: break
        PrimeFactorization(n)
        lst = []
        a = 1
        for i in range(0 , tot_pf - 1):
            if pf_list[i] == pf_list[i + 1]:
                a += 1
            else:
                lst.append([pf_list[i] , a])
                a = 1
        lst.append([pf_list[tot_pf - 1] , a])
        x = len(lst)
        for i in range(0 , x - 1):
            sys.stdout.write(str(lst[i][0]) + "^" + str(lst[i][1]) + " ")
        sys.stdout.write(str(lst[x - 1][0]) + "^" + str(lst[x - 1][1]) + "\n")
main()
