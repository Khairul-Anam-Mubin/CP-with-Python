import math
import sys
input = sys.stdin.readline
def inlist():
    return(list(map(int,input().split())))

def BigMod(b , p , m):
    if (p == 0): return 1
    if (p % 2 == 0):
        s = BigMod(b , p / 2 , m)
        return (((s % m) * (s % m)) % m)
    else: 
        return (((b % m) * (BigMod(b , p - 1 , m) % m)) % m)
def main():
    lst = inlist()
    print(BigMod(lst[0] , lst[1] , lst[2]))
main()
    
    
