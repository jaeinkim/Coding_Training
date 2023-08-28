import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        v_s = collections.Counter(s)
        v_t = collections.Counter(t)
        return v_s == v_t