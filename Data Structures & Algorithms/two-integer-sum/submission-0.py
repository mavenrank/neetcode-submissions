class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_value, j_value = 0,0
        for i in range (len(nums)):
            for j in range (len(nums)):
                if nums[i] + nums[j] == target:
                    if i == j:
                        pass
                    else:
                        i_value,j_value = i,j
                        return [i_value, j_value]
        
        return [i_value, j_value]