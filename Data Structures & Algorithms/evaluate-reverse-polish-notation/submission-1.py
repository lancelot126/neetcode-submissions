class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                num1 = int(stack[-2])
                num2 = int(stack[-1])
                stack.pop()
                stack.pop()
                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                elif tokens[i] == "/":
                    stack.append(num1 / num2)
            else:
                stack.append(tokens[i])
        return int(stack[0])