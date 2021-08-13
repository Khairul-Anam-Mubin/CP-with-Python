import math
import sys
input = sys.stdin.readline
def Gcd(a , b):
    if (a < 0): return Gcd(-a , b)
    if (b < 0): return Gcd(a , -b)
    if (b == 0): return a
    return Gcd(b , a % b)
def Lcm(a , b):
    g = Gcd(a , b)
    return ((a // g) * b)
def main():
    a = int(input())
    b = int(input())
    print(Lcm(a , b))
    
    # just for check. edited by iqbal
main()
    
