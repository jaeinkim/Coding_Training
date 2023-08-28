# 1. collections 시도
# import collections
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         v_s = collections.Counter(s)
#         v_t = collections.Counter(t)
#         return v_s == v_t


# 2. hm 이용
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:

        hm_s = collections.Counter(s)
        hm_t = collections.Counter(t)
        return v_s == v_t