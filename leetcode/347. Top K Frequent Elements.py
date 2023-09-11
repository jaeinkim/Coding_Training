

# 첫 시도 - 실패
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = collections.defaultdict(int)
        for n in nums:
            hm[n] += 1
        print(hm)
        hm2 = dict(zip(hm.values(), hm.keys()))
        print(hm2)
        arr = sorted(list(hm.values()), reverse=True)
        answer = []
        for i in range(0, k):
            answer.append(hm2[arr[i]])
        return answer

