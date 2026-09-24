from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        out = []
        
        for ele in count.most_common(k):
            out.append(ele[0])

        return out