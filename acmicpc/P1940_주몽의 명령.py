#책의 코드
# import sys
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# A = list(map(int, input().split()))
# A.sort()
# count = 0
# i = 0
# j = N - 1
#
# while i < j: # 투 포인터 이동 원칙 따라 포인터를 이동하며 처리
#     if A[i] + A[j] < M:
#         i += 1
#     elif A[i] + A[j] > M:
#         j -= 1
#     else:
#         count += 1
#         i += 1
#         j -= 1
#
# print(count)


# 나의 코드 - 틀림
# import sys
# input = sys.stdin.readline
# n  = int(input())
# m = int(input())
# lst = sorted(list(map(int, input().split())))
#
# start_index = 0
# end_index =1
# count = 0
# sum  = lst[start_index] + lst[end_index]
#
# while end_index < len(lst)-1:
#     if sum == m:
#         count += 1
#         sum -= lst[end_index]
#         end_index +=1
#         sum +=  lst[end_index]
#     elif sum > m:
#         sum-= lst[start_index]
#         start_index += 1;
#         sum+= lst[start_index]
#     elif sum < m:
#         sum -= lst[end_index]
#         end_index +=1
#         sum += lst[end_index]
#
# print(count)


# 나의 코드 - 정답 보고 나서 코드 복기
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = sorted(list(map(int, input().split())))

count = 0
i  = 0
j = N-1

while i < j:
    if A[i] + A[j] < M:
        i+=1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count+=1
        i+=1
        j -=1
print(count)
