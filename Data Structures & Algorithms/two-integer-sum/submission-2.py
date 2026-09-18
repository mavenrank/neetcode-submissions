class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)):
            num = nums[i]
            req_value = target-num
            if req_value in seen:
                return [seen[req_value], i]
            seen[num]=i
                        

                    

