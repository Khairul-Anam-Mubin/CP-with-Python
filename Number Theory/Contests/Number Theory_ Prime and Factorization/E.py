# Problem Link: https://vjudge.net/contest/444859#problem/E
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))
    
def main():
    n = int(input())
    ans = [0]
    for i in range(n):
        ans += [0]
    ans[0] = 0;
    ans[1] = 1
    ans[2] = 2
    ans[3] = 0
    for i in range(4 , n + 1):
        x = i
        sq = int(math.sqrt(x))
        for j in range(sq , 1 , -1):
            if x % j == 0: 
                ans[x] = ans[j] + ans[x // j]
                break
    sys.stdout.write(str(ans[n]) + "\n")
main()
    
