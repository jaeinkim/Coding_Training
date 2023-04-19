# # acmicpc
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# answer = 0
# print(answer)
#
#
# # pytest를 활용하기 위한 문법
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         return [1,2,3]
#


def solution(A):
    A.sort()  # 주어진 배열을 정렬합니다.
    smallest = 1  # 최소 양의 정수는 1부터 시작합니다.

    for num in A:
        if num == smallest:  # num이 smallest와 같으면 다음으로 넘어갑니다.
            smallest += 1
        elif num > smallest:  # num이 smallest보다 크면 최소 양의 정수를 찾았습니다.
            return smallest
    return smallest  # 모든 요소가 배열에 있을 경우, 다음 양의 정수를 반환합니다.

A = [1, 2, 3]
print(solution(A))