# Problem Link: https://vjudge.net/contest/444859#problem/D
import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

def Sieve(mxN):
    isp = []
    for i in range(0 , mxN + 1):
        if (i > 2 and i % 2 == 0):
            isp.append(1)
        else:
            isp.append(0)
    sq = int(math.sqrt(mxN))
    isp[0] = isp[1] = 1
    for i in range(3 , sq , 2):
        if isp[i] == 0:
            for j in range(i * i , mxN , i + i):
                isp[j] = 1
    prime = []
    prime.append(2)
    for i in range(3 , mxN , 2):
        if isp[i] == 0:
            prime.append(i)
    return prime
def main():
    prime = Sieve(90000000)
    #print(len(prime))
    t = int(input())
    for i in range(0 , t):
        q = int(input())
        sys.stdout.write(str(prime[q - 1]) + "\n")
main()
    
