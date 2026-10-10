class Solution:
    def isValid(self, s: str) -> bool:
        brackets={")":"(", "}":"{", "]":"["}
        stack=[]
        for char in s:
                
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if len(stack)==0:
                    return False
                else:
                    top=stack[-1]
                    if brackets[char]==top:
                        stack.pop()
                    else:
                        return False
                
        if len(stack)==0:
            return True
        else:
            return False