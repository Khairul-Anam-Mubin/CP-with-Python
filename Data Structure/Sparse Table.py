import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

def main():
    n , q = map(int,input().split())
    ar = inlist()
    sptab = []
    k = int(math.log2(n))
    for j in range(k + 1):
        tmp = []
        for i in range(n + 1):
            tmp.append(-1)
        sptab.append(tmp)
    for i in range(n):
        sptab[0][i] = ar[i]
    for j in range(1 , k + 1):
        for i in range(0 , n - (1 << j) + 1):
            sptab[j][i] = min(sptab[j - 1][i] , sptab[j - 1][i + (1 << (j - 1))]);
    for tc in range(q):
        a , b = map(int , input().split())
        a -= 1
        b -= 1
        len = int(math.log2(b - a + 1))
        ans = min(sptab[len][a] , sptab[len][b - (1 << len) + 1])
        print(ans)
main()