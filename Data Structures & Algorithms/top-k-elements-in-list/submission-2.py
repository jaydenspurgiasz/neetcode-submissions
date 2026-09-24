from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1

        return sorted(counts, key=counts.get, reverse=True)[:k]