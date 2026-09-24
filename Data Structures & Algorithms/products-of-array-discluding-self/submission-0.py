class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        p = 1
        for i in range(len(nums)):
            pre.append(p)
            p *= nums[i]
        
        suf = [0] * len(nums)
        s = 1
        for i in range(len(nums)):
            suf[len(nums) - i - 1] = s
            s *= nums[len(nums) - i - 1]

        out = []
        for i in range(len(pre)):
            out.append(pre[i] * suf[i])
        
        return out