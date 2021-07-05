#Problem Link : https://vjudge.net/contest/444859#problem/T
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
def GetNod():
    nod = []
    mxN = 1000000
    for i in range(0 , mxN + 1):
        nod.append(0)
    for i in range(1 , mxN + 1):
        for j in range(i , mxN + 1 , i):
            nod[j] = nod[j] + 1;
    return nod
def main():
    nod = GetNod()
    t = int(input())
    for i in range(0 , t):
        ab = inlist()
        a = ab[0]
        b = ab[1]
        g = Gcd(a , b)
        sys.stdout.write(str(nod[g]) + "\n")
main()
