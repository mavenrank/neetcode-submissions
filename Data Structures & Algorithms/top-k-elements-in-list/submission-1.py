class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict=defaultdict(int)
        for num in nums:
            num_dict[num]=num_dict.get(num,0)+1
        
        items = list(num_dict.items())
        #gives all of the key:values inside the dict outputted as LIST
        items.sort(key = lambda x : x[1], reverse=True)
        # imagine if itme is [(1,1), (2,2), (3,3)]
        #x[1] looks at every value
        # sort takes two args, 1 is the KEY to use for sorting, 2 is reverse yes or no
        # we are putting key as the values from x[1]
        # and reverse = true as we want it to be ordered 5,4,3,2,1 in this way
        #items sort will give us [(3,3), (2,2), (1,1)]

        l=[]
        for x in range(k):
            #let it run only until the freq required
            l.append(items[x][0]) 
            # x is (3,3), x[0] is the first three 
        return l
        
