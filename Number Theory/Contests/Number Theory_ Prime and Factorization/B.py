# Problem Link: https://vjudge.net/contest/444859#problem/B
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

def PreCal():
    isp = []
    mxN = 10000
    for i in range(mxN + 1):
        isp.append(0)
    for i in range(2 , mxN + 1):
        if isp[i] == 0:
            for j in range(i , mxN + 1, i):
                isp[j] = isp[j] + 1
    ans = []
    for i in range(1 , mxN + 1):
        if isp[i] >= 3:
            ans.append(i)
    return ans

def main():
    lst = PreCal()
    #print(lst)
    #sys.stdout.write(str(len(lst)))
    t = int(input())
    for i in range(t):
        n = int(input())
        sys.stdout.write(str(lst[n - 1]) + "\n")
main()
    
