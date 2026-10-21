class Solution:
    def minWindow(self, s: str, t: str) -> str:

        best_length=math.inf
        best_l=0
        best_r=0
        count_current_s=defaultdict(int)
        count_t=defaultdict(int)
        for tchar in t:
            count_t[tchar]+=1

        required=len(count_t)
        satisfied=0
        l=0
        for r in range(len(s)):
            current=s[r]
            count_current_s[current]+=1
            if current in count_t:
                if count_current_s[current]==count_t[current]:
                    satisfied+=1
            
            while (satisfied==required):
                current_length=len(s[l:r+1])
                if current_length<best_length:
                    best_length=current_length
                    best_l=l
                    best_r=r

                left_char=s[l]
                count_current_s[left_char]-=1 

                if left_char in count_t:
                        if count_current_s[left_char] < count_t[left_char]:
                            satisfied -= 1
                if count_current_s[left_char]==0:
                    del count_current_s[left_char]
                l+=1

        if best_length==math.inf:
            return ""
        return s[best_l:best_r+1] 