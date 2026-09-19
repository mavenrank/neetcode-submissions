class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [0] * 26
        t_list = [0] * 26
        for i in range(len(s)):
            s_list[ord(s[i])%26] += 1
        
        for i in range(len(t)):
            t_list[ord(t[i])%26] +=1

        if (s_list == t_list):
            return True
        else:
            return False