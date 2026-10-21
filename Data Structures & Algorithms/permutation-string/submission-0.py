class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1=defaultdict(int)
        count_s2=defaultdict(int)
        l=0
        for s in s1:
            count_s1[s]+=1

        for r in range(len(s2)):
            count_s2[s2[r]]+=1
            window_length=r-l+1
            if window_length>len(s1):
                count_s2[s2[l]]-=1
                if count_s2[s2[l]]==0:
                    del count_s2[s2[l]]
                l+=1

            window_length=r-l+1
            
            if window_length==len(s1):
                if count_s1==count_s2:
                    return True
        return False