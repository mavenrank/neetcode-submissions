class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        excluded_index=0
        outputs=[1]*len(nums)
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)

        len_nums=len(nums)
        for i in range(len(nums)-1):
            if i==0:
                pass
            else:
                left_products[i]=nums[i-1]*left_products[i-1]
                idx=len(nums)-1-i
                right_products[len(nums)-1-i]=nums[idx+1]*right_products[idx+1]
                
        for i in range(len(nums)-1):
            outputs[i]=left_products[i]*right_products[i]
        return outputs


