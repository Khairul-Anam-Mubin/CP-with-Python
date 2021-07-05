# Problem Link: https://vjudge.net/contest/444859#problem/H
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
def Sieve():
    isp = []
    mxN = 1000001
    for i in range(0 , mxN):
        isp.append(1)
    for i in range(4 , mxN , 2):
        isp[i] = 0
    sq = int(math.sqrt(mxN)) + 1
    for i in range(3 , sq , 2):
        if isp[i]:
            for j in range(i * i, mxN , i + i):
                isp[j] = 0
    return isp   
def main():
    dp = Sieve()
    dp[0] = 0
    for i in range(1 , len(dp)):
        dp[i] += dp[i - 1]
    t = int(input())
    n = inlist()
    for i in range(0 , t):
        sq = int(math.sqrt(n[i]))
        ans = 1
        ans = dp[n[i]] - dp[sq]
        ans += 1
        sys.stdout.write(str(ans) + "\n")
main()
