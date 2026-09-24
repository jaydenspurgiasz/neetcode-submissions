'''
O(n) requirement -> regular loops, no nested

Init a set
Loop:
    -Throw every number into a set

Loop:
    -



'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        starts = []
        for num in nums:
            if num - 1 not in seen:
                starts.append(num)
        
        high = 0
        for n in starts:
            l = 1
            while n + l in seen:
                l += 1
            if l > high:
                high = l
        
        return high





