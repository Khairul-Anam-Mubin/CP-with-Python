#problem link : https://vjudge.net/contest/444859#problem/V
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

mxN = 1000001
nod = []
def SieveOfDivisors():
    global nod
    for i in range(0 , mxN):
        nod.append(0)
    for i in range(1 , mxN):
        for j in range(i , mxN , i):
            nod[j] += 1
def main():
    SieveOfDivisors()
    vis = []
    for i in range(0 , mxN + 1):
        vis.append(1)
    for i in range(1 , mxN):
        for j in range(i , mxN , i):
            if (nod[j] <= 3 or nod[j] % nod[i] != 0):
                vis[j] = 0
    ans = []
    for i in range(1 , mxN):
        if vis[i]:
            ans.append(i)
    for i in range(107 , len(ans) , 108):
        sys.stdout.write(str(ans[i]) + "\n")
main()
