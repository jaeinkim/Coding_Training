# '틀렸습니다' 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = []
prefix_sum = [[0]]

for i in range(n):
    numbers.append(list(map(int, input().split())))


for n in numbers:
    prefix_sub_sum = [0]
    temp = 0
    for m in n:
        temp = temp + m
        prefix_sub_sum.append(temp)
    prefix_sum.append(prefix_sub_sum)

for i in range(m):
    a, b, c, d = list(map(int, input().split()))
    sum = 0
    for i in range(c):
        if i+1 >= a:
            sum = sum + prefix_sum[i+1][d] - prefix_sum[i+1][b-1]
    print(sum)

# 책의 코드
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# A = [[0]*(n+1)]
# D = [[0]*(n+1) for _ in range(n+1)]
#
# for i in range(n):
#     A_row = [0] + [int(x) for x in input().split()]
#     A.append(A_row)
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         # 합 배열 구하기
#         D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
#
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     # 구간 합 배열로 질의에 답변
#     result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
#     print(result)


# 내가 복기한 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1])
