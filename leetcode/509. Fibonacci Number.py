# 1. 재귀 구조 브루트 포스
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <=1: return n
#         return self.fib(n-1) + self.fib(n-2)

# 2. 메모이제이션: 하향식 방법
# class Solution:
#     dp = collections.defaultdict(int)
#     def fib(self, n: int) -> int:
#         if n <=1: return n
#         if self.dp[n]: return self.dp[n]
#         self.dp[n] = self.fib(n-1) + self.fib(n-2)
#         return self.dp[n]

# 3. 타뷸레이션: 상향식 방법
### 1) 책 풀이
# class Solution:
#     dp = collections.defaultdict(int)

#     def fib(self, n: int) -> int:
#         self.dp[0] = 0
#         self.dp[1] = 1
#         for i in range(2, n+1):
#             self.dp[i] = self.dp[i-1] + self.dp[i-2]
#         return self.dp[n]

### 2) 나의 첫 풀이
# class Solution:
#     def fib(self, n: int) -> int:
#         if n < 1:
#             return 0
#         lst = [0]*(n+1)
#         lst[1] = 1

#         for i in range(2, n+1):
#             lst[i] = lst[i-1] + lst[i-2]
#         return lst[n]

# 4. 두 변수만 이용해 공간 절약
# class Solution:
#     def fib(self, n: int) -> int:
#         x, y = 0, 1
#         for i in range(0, n):
#             x, y = y, x+y
#         return x

# 행렬로 푸는 방식 - 걍 몰라도 될 것같아 무시함. 책에서도 참고하라고 함
# class Solution:
#     def fib(self, n: int) -> int:
        