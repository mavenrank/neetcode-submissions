class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            req_value = target-nums[i]
            if req_value in seen:
                return [seen[req_value], i]
            seen[nums[i]]=i
                        

                    

