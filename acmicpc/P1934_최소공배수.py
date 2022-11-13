# 책의 풀이


# 나의 풀이
import sys
input = sys.stdin.readline

n = int(input())

def gcd(n, m):
    answer = 0
    if n%m == 0:
        return m
    else:
        return gcd(m, n%m)



for i in range(n):
    n, m = map(int, input().split())
    print(int(n*m/gcd(n,m)))


