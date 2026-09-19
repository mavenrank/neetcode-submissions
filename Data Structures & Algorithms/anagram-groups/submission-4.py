class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dicts = defaultdict(list) #defaultdict has capability to actually create <arg> when the item isnt found in the dict

        for word in strs:
            # sorted(word) gives output list after sorting the values aka "cat" -> ['a', 'c', 't']
            #now append it to an empty word -> ['a','c','t'] => act
            #sortedword = act
            #str_dicts[sorted_word] refers to values of the key in that dict, now we append that actual word that we sorted.
            #essentially take word, sort it, get it back into string. cuz sorting works as the signature for us that will be same for each of these words that are anagrams
            #so it becomes, act : ['cat', 'act']
            # and when we get 'post', it turns into 'opst' as the signature as its not alreadypresent, it creates a new key and we append 'post to the values

            str_dicts["".join(sorted(word))].append(word)
        return list(str_dicts.values())

            

        