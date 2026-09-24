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
        ana = {} # Map: sorted string -> index in out

        # Use sorted approach
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s in ana:
                out[ana[s]].append(strs[i])
            else:
                out.append([strs[i]])
                ana[s] = len(out) - 1
        
        return out
                
