class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=0
        current_area=None
        while (l<r):
            current_area=min(heights[l], heights[r]) * (r-l)
            
            if (heights[l]<heights[r]):
                l+=1
            elif (heights[r]<heights[l]):
                r-=1
            else:
                r-=1
            if current_area > max_area:
                max_area = current_area

        return max_area


