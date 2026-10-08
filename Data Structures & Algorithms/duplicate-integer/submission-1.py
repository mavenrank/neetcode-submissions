class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for x in nums:
            if x in seen:
                seen[x]=seen[x]+1
            else:
                seen[x]=1
        
        flag = False
        for k, v in seen.items():
            if v == 2:
                flag = flag or True
        
        if flag == True:
            return True
        else:
            return False
            