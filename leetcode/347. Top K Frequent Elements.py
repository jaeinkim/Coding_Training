

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


# 정답보고 해서 성공
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 이중 어레이를 써보자.  어레이의 인덱스를 카운트로 하자
        lst = [[] for i in range(len(nums)+1)]
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        for K, V in hm.items():
            lst[V].append(K)

        answer = []

        for i in range(len(lst)-1,-1,-1):
            k = k - len(lst[i])
            answer = answer + lst[i]
            if  k == 0:
                return answer





