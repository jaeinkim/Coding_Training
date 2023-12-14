# https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence
# Medium
#
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
#
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# 23/12/8 금. 해설 보고 품
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n-1 not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


# 23/12/15 금. 복기 시도 결과 Time Limit Exceeded. 처음시작이지 않은 것들을 순회하는 것들이니 거의 무조건 이중으로 돈다고 생각하는 잘못된 로직이네....
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        length = 0

        for n in nums:
            length = 1
            if n-1 not in numSet:
                continue
            while n + length in numSet:
                length +=1
            longest = max(length+1, longest)
        return length if longest == 0 else longest # 아예 0건인 경우를 위한 로직