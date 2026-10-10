class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        conseq_set=set(nums)
        count=1
        current=1
        start=1
        longest=0
        for num in conseq_set:
            if num-1 in conseq_set:
                continue
            start=num
            current=start
            count=1
            while (current+1 in conseq_set):
                count+=1
                current+=1
                if (count > longest):
                    longest=count
            count=1
        return longest

            
            