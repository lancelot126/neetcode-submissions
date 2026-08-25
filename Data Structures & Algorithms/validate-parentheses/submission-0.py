class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingChar = { '}' : '{', ']' : '[', ')' : '('}

        for c in s:
            if c in closingChar:
                if stack and stack[-1] == closingChar[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False