class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=sorted(nums)
        o=set([])
        y=None
        z=None
        for idx in range(len(s)-2):
            x=idx
            y=idx+1
            z=len(s)-1
            while (y<z):
                if s[y]+s[z]<-s[x]:
                    y+=1
                elif s[y]+s[z]>-s[x]:
                    z-=1
                else:
                    o.add((s[x],s[y],s[z]))
                    y+=1
                    z-=1

        outputlist=[]    
        for tuples in o:
            outputlist.append(list(tuples))
        
        return outputlist