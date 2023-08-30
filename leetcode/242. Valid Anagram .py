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
        hm_s = {}
        hm_t = {}
        for c in s:
            hm_s[c] = hm_s.get(c, 0) + 1
        for c in t:
            hm_t[c] = hm_t.get(c, 0) + 1
        print(hm_s, hm_t)
        return hm_s == hm_t


