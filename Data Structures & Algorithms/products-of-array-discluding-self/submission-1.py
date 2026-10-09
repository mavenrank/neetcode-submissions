class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        excluded_index=0
        outputs=[1]*len(nums)
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)

        len_nums=len(nums)
        for i in range(1,len(nums)):
            left_products[i]=nums[i-1]*left_products[i-1]
                
        for i in range(len(nums)-1-1, -1, -1):
            right_products[i]=nums[i+1]*right_products[i+1]
                
        for i in range(len(nums)):
            outputs[i]=left_products[i]*right_products[i]
        return outputs


