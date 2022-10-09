# # 시간 초과 코드
# import sys
# input = sys.stdin.readline
# [n, m] = list(map(int, input().split(' ')))
# mylist = list(map(int, input().split(' ')))
# sum_list = [0 for i in range(n)]
# for i in range(n):
#     if i == 0:
#         sum_list[i] = mylist[i]
#     sum_list[i] = sum_list[i-1] + mylist[i]
#
# for a in range(m):
#     [i, j] = list(map(int, input().split(' ')))
#     if i == 1:
#         print(sum_list[j-1] )
#     else:
#         print(sum_list[j-1] - sum_list[i-1-1])

# 책의 코드
import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)     # 합 배열 만들기

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
