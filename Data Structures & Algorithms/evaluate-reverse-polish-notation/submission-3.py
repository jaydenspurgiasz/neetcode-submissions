class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                s.append(s.pop() + s.pop())
            elif tokens[i] == "-":
                num = s.pop()
                s.append(s.pop() - num)
            elif tokens[i] == "*":
                s.append(s.pop() * s.pop())
            elif tokens[i] == "/":
                num = s.pop()
                s.append(int(s.pop() / num))
            else:
                s.append(int(tokens[i]))

        return s[0]