#problem link : https://vjudge.net/contest/444859#problem/X
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
def main():
    Sieve()
    t = int(input())
    for tc in range(1 , t + 1):
        n = int(input())
        sz = len(prime)
        ans = []
        for i in range(0 , sz):
            if prime[i] > n: break
            cnt = 0
            x = n
            p = prime[i]
            while (x // p):
                cnt += x // p
                x //= p
            ans.append([prime[i] , cnt])
        sys.stdout.write("Case " + str(tc) + ": " + str(n) + " = ")
        #print(ans)
        sz = len(ans)
        for i in range(0 , sz - 1):
            sys.stdout.write(str(ans[i][0]) + " (" + str(ans[i][1]) + ") * ")
        sys.stdout.write(str(ans[sz - 1][0]) + " (" + str(ans[sz - 1][1]) + ")\n")
main()
