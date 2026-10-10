class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        total_area=0
        maxi=0
        water=[0]*len(height)
        for i in range(len(height)):
            if height[i]>maxi:
                maxi=height[i]
            lmax[i]=maxi
        maxi=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>maxi:
                maxi=height[i]
            rmax[i]=maxi

        for i in range(len(height)):
            water=min(lmax[i],rmax[i])-height[i]
            total_area+=water

        return total_area
