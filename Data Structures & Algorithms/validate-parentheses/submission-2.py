class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or  ch == '{' or  ch == '[':
                stack.append(ch)
            else:
                if len(stack) < 1:
                    return False
                end = stack.pop()
                if not ((ch == ')' and end == '(') or (ch == ']' and end == '[') or (ch == '}' and end == '{')):
                    return False

        return len(stack) == 0
