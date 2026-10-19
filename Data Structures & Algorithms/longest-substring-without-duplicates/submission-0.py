class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        window=set()
        best=0
        i=0
        for i in range(len(s)):
            current=s[i]
            while current in window:    
                window.discard(s[l])
                l+=1
            window.add(current)

            current_length=i-l+1
            if current_length>best:
                best=current_length
        return best
            