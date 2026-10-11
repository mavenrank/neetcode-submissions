class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            curr_temp=temperatures[i]
            while stack and curr_temp > temperatures[stack[-1]]:
                top=stack[-1]
                result[top]=i-top
                stack.pop()
            stack.append(i)

        return result
