# Problem Link: https://vjudge.net/contest/444859#problem/F
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

def Sieve():
    mxN = 10000000
    isp = []
    for i in range(0 , mxN + 1):
        isp.append(1)
    for i in range(4 , mxN + 1, 2):
        isp[i] = 0
    for i in range(3 , mxN + 1, 2):
        if isp[i] == 1:
            for j in range(i * i, mxN + 1, i + i):
                isp[j] = 0
    for i in range(1 , mxN + 1):
        isp[i] += isp[i - 1]
    return isp
def main():
    dp = Sieve()
    t = int(input())
    for i in range(t):
        n = int(input())
        ans = dp[n] - dp[(n // 2)]
        sys.stdout.write(str(ans) + "\n")
main()
