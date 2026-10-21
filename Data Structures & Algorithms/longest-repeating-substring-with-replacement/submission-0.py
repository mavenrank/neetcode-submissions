class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window=set()
        best=0
        dict_counts=defaultdict(int)
        length_of_current_substring=0
        l=0
        for r in range(len(s)):
            current=s[r]
            dict_counts[current]+=1
            highest_count=max(dict_counts.values())
            length_of_current_substring=r-l+1
            repl_needed=length_of_current_substring-highest_count
            if repl_needed>k:
                dict_counts[s[l]]-=1
                if dict_counts[s[l]] == 0:
                    del dict_counts[s[l]]
                l+=1
                length_of_current_substring=r-l+1
            if length_of_current_substring>best:
                best=length_of_current_substring
        return best
