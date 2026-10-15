class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest_k=1
        highest_k=max(piles)
        hours=0
        best_k=highest_k
        while lowest_k <= highest_k:
            hours=0
            middle_k=lowest_k + ((highest_k-lowest_k)//2)
            for pile in piles:
                if pile%middle_k !=0:
                    hours+=1
                hours+=pile//middle_k

            if hours > h:
                lowest_k=middle_k+1
            else:
                highest_k = middle_k-1
                if middle_k <= best_k:
                    best_k=middle_k
        return best_k
            
