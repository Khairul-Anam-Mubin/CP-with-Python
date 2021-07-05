# Problem Link : https://vjudge.net/contest/444859#problem/K
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
    
def main():
    n = int(input())
    ans = 0
    for i in range(1 , n + 1):
        x = 2
        cnt = 0
        k = i
        while (x * x <= k):
            if (k % x == 0):
                cnt += 1
                while (k % x == 0):
                    k /= x
            x += 1
        if (k != 1): cnt += 1
        if (cnt == 2): ans += 1
    sys.stdout.write(str(ans) + "\n")
main()
