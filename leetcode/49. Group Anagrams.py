# 49. Group Anagrmas

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]

# 첫 시도 - 실패
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        sub_answer =[]
        strs.sort()
        for i in range(1, len(strs)):
            if collections.Counter(strs[i-1]) == collections.Counter(strs[i]):
                sub_answer.append(strs[i-1])
            else:
                sub_answer.append(strs[i-1])
                answer.append(sub_answer)
                sub_answer = []
                sub_answer.append(strs[i-1])

        answer.append(sub_answer)
        return answer


# 두번째 시도 - 정답보고 함
class 함olution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = [0 for _ in range(26)]
        hm = {}
        for s in strs:
            for c in s:
                lst[ord(c) - ord('a')] += 1
            k = tuple(lst)
            # print(k)
            hm[k] = hm.get(k, []) + [s]
            lst = [0 for _ in range(26)]
        return hm.values()

# 세번째 시도 - 정답보고 함
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()