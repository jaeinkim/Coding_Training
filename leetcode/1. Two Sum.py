# 투포인터 문제 아니여?!
from typing import List

# 나의 풀이
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = dict()
        sub = 0
        for key, value in enumerate(nums):
            dict_nums[value] = dict_nums.get(value, []) + [key]
            # print(key, value)
            # print(dict_nums[value])
            if len(dict_nums[value]) > 1 and value*2 == target:
                return [dict_nums[value][0], dict_nums[value][1]]
        for i in range(len(nums)):
            sub = target - nums[i]
            if len(dict_nums.get(sub, [])) !=0 and i != dict_nums.get(sub)[0]:
                return (i, dict_nums.get(sub)[0])

sol = Solution()
sol.twoSum([3,3], 6)
# 1. Brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target -nums[i]:
                    return [i, j]

# 2. Two-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


# 3. One-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i