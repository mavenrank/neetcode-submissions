class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dicts = {}

        for i in range(len(strs)):
            word = strs[i]
            list_for_word = [0]*26
            for ch in word:
                list_for_word[ord(ch)-ord('a')]+=1
            signature = tuple(list_for_word)
            # str_dicts[signature]
            if signature not in str_dicts:
                str_dicts[signature]=[]
            str_dicts[signature].append(word)

        return list(str_dicts.values())

            

        