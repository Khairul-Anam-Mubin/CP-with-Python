#Problem Link: https://vjudge.net/contest/444859#problem/J
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

def Gcd(a , b):
    r = 0
    while b != 0:
        r = b
        b = a % b
        a = r;
    return a
def main():
    isp = []
    mxN = 10000001
    for i in range(0 , mxN):
        isp.append(0)
    for i in range(2 , mxN):
        if isp[i] == 0:
            for j in range(i + i, mxN, i):
                if isp[j] == 0:
                    isp[j] = i
    n = int(input())
    ar = inlist()
    ans1 = []
    ans2 = []
    for i in range(n):
        a = -1
        b = -1
        if isp[ar[i]] != 0:
            tmp = isp[ar[i]]
            b = ar[i]
            a = 1
            while b % tmp == 0:
                b //= tmp
                a *= tmp
            if b == 1:
                a = -1
                b = -1
            else:
                if Gcd(a + b , ar[i]) != 1:
                    a = -1
                    b = -1
        ans1.append(a)
        ans2.append(b)
    for i in range(0 , n):
        sys.stdout.write(str(ans1[i]) + " ")
    sys.stdout.write("\n")
    for i in range(0 , n):
        sys.stdout.write(str(ans2[i]) + " ")
    sys.stdout.write("\n")
main()
