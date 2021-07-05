#Problem Link : https://vjudge.net/contest/444859#problem/A
import sys
input = sys.stdin.readline

def PreCal():
    mxN = 10000000
    dp = []    
    for i in range(0 , mxN + 1):
        dp.append(0)
    for i in range(2 , mxN + 1):
        if dp[i] == 0:
            for j in range(i , mxN + 1, i):
                if dp[j] == 0:
                    dp[j] = i
    for i in range(2 , mxN + 1):
        dp[i] += dp[i - 1]
    return dp
def main():
    dp = PreCal()
    t = int(input())
    for i in range(t):
        n = int(input())
        sys.stdout.write(str(dp[n]) + "\n")
main()
