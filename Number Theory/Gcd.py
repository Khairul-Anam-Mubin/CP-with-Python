import math
import sys
input = sys.stdin.readline
def Gcd(a , b):
    if (a < 0): return Gcd(-a , b)
    if (b < 0): return Gcd(a , -b)
    if (b == 0): return a
    return Gcd(b , a % b)
def main():
    a = int(input())
    b = int(input())
    print(Gcd(a , b))
main()
    
