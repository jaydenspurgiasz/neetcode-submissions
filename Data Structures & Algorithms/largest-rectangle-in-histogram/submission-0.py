class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        m = 0
        s = [-1]
        for i in range(len(heights)):
            # calc all terminating rects
            while len(s) > 0 and heights[s[-1]] > heights[i]:
                a = heights[s.pop()] * (i - s[-1] - 1)
                if a > m:
                    m = a
            
            s.append(i)
        
        return m
