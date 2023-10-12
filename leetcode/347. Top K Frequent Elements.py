

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

        for K, V in hm.items(): # 소문자 k로 하면 해당 포문 값으로 덮어 씌워짐
            lst[V].append(K)

        answer = []

        for i in range(len(lst)-1,-1,-1):
            k = k - len(lst[i])
            answer = answer + lst[i]
            if  k == 0:
                return answer


# 복기해서 푼 것
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_lst = [[] for _ in range(len(nums)+1)]
        hm = {}

        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        for K, V in hm.items():
            count_lst[V].append(K)
        answer = []
        print(count_lst)
        for i in range(len(count_lst)-1, 0, -1):
            if len(count_lst[i]) != 0:
                answer = answer + count_lst[i]
                k -= len(count_lst[i])

            if k == 0:
                return answer
# 23/9/19 재풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        cnt_lst = [[] for _ in range(len(nums)+1)]
        answer = []
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        for K, V in hm.items():
            cnt_lst[V].append(K)
        print(cnt_lst)
        for i in range(len(cnt_lst)-1, -1, -1):
            if k == 0:
                return answer
            if len(cnt_lst[i]) == 0: # if cnt_lst is None은 안됨
                continue
            answer = answer + cnt_lst[i]
            k -= len(cnt_lst[i])

#9/20 수. 재풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        cnt_lst = [[] for _ in range(len(nums)+1)]
        answer = []

        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        for K, V in hm.items():
            cnt_lst[V].append(K)

        for i in range(len(cnt_lst)-1, 0, -1):
            answer = answer + cnt_lst[i]
            if k == len(answer):
                return answer



# 9/20 정답 풀이
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res







