class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char in "+-*/":
                s=stack.pop()
                f=stack.pop()
                if char == '+':
                    stack.append(f+s)
                elif char == '-':
                    stack.append(f-s)
                elif char == '*':
                    stack.append(f*s)
                elif char == '/':
                    stack.append(f/s)
                
            else:
                stack.append(int(char))
        
        return stack[-1]
