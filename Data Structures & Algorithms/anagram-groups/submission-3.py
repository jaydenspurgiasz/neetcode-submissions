class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chs = [0] * 26
        for i in range(len(s)):
            chs[ord(s[i]) - ord('a')] += 1
            chs[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(chs)):
            if chs[i] != 0:
                return False
        
        return True

        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        ana = {}

        for i in range(len(strs)):
            chs = [0] * 26
            for ch in strs[i]:
                chs[ord(ch) - ord('a')] += 1
        
            key = tuple(chs)
            if key in ana:
                out[ana[key]].append(strs[i])
            else:
                ana[key] = len(out)
                out.append([strs[i]])
        
        return out
                
