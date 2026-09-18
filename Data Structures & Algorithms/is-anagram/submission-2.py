class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for letter in s:
            count_letter = s.count(letter)
            s_dict[letter] = count_letter
        
        for letter in t:
            count_letter = t.count(letter)
            t_dict[letter] = count_letter

        flag = True

        if len(s_dict) != len(t_dict):
            return False
        else:
            for character in s_dict:
                if character not in t_dict:
                    return False
                else:
                    if s_dict[character] == t_dict[character]:
                        flag = flag and True
                    else: 
                        flag = False

            for character in t_dict:
                if character not in s_dict:
                    return False
                else: 
                    if s_dict[character] == t_dict[character]:
                        flag = flag and True
                    else: 
                        flag = False
        
        return flag
        # else:
        #     for x in s_dict:
        #         if s_dict[x] == t_dict[x]:
        #             flag = flag and True
        #         else:
        #             flag = flag and False    

        # return flag  