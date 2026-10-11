class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h=0
        w=0
        stack=[]
        max_area=0
        for i in range(len(heights)):
            if not stack:
                stack.append(i)
            else:
                while stack and heights[i]<heights[stack[-1]]:
                    top=stack[-1]
                    stack.pop()
                    if stack:
                        left=stack[-1]
                    else:
                        left=-1
                    right=i
                    width=right-left-1
                    area=heights[top]*width
                    max_area = max(max_area, area)
                stack.append(i)
    
        right = len(heights)
        while stack:
            top = stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1
            width = right - left - 1
            area = heights[top] * width
            max_area = max(max_area, area)

        return max_area
                    