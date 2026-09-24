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
        
        ana = defaultdict(list)

        for i in range(len(strs)):
            chs = [0] * 26
            for ch in strs[i]:
                chs[ord(ch) - ord('a')] += 1
        
            ana[tuple(chs)].append(strs[i])
            
        
        return list(ana.values())
                
