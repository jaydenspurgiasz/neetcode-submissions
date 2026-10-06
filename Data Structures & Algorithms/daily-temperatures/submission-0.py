'''
30,38,30,36,35,40,28
When on i, add it to the stack
Now on i+1 we can check if its warmer.
    If it is, then pop the previous element and update result[i] with 1
    Otherwise, add i+1 to stack
Repeat with i+etc

40 28
1 4 1 2 1 0 0

Works, just need to also track index

30,38,30,36,35,40,28
i = 1

'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return [0]

        s = [[temperatures[0], 0]]
        result = [0] * len(temperatures)

        i = 1
        while i < len(temperatures):
            if len(s) > 0 and s[-1][0] < temperatures[i]:
                result[s[-1][1]] = i - s[-1][1]
                s.pop()
            else:
                s.append([temperatures[i], i])
                i += 1
            
        
        return result
