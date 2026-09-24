class Solution:
    # Turn each string into array of ints. 256 valid characters
    def encode(self, strs: List[str]) -> str:
        out = ""
        
        for st in strs:
            for ch in st:
                out += (str(ord(ch)) + ",")
            out += ("256,")

        return out

    def decode(self, s: str) -> List[str]:
        out = []

        st = ""
        for ch in s.split(",")[:-1]:
            if ch == "256":
                out.append(st)
                st = ""
            else:
                st += chr(int(ch))
            
        return out
