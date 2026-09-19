class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict=defaultdict(int)
        for num in nums:
            num_dict[num]=num_dict.get(num,0)+1
        
        items = list(num_dict.items())
        items.sort(key = lambda x : x[1], reverse=True)
        l=[]
        for x in range(k):
            l.append(items[x][0])
        return l
        
