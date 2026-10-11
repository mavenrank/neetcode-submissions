class Solution:
    def isValid(self, s: str) -> bool:
        brackets={
            "[":"]", "(":")", "{":"}"
        }
        stack = []
        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            elif not stack or stack.pop() != char:
                return False
        return not stack