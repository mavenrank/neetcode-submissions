class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes=[]
        for i in range(len(strs)):
            sizes.append(len(strs[i]))

        sizes_str=",".join(str(x) for x in sizes)
        all_words="".join(strs)
        encoded_string=sizes_str+"#"+all_words
        return encoded_string
        
    def decode(self, s: str) -> List[str]:

        sizes_str, words = s.split("#", 1)
        
        sizes=sizes_str.split(",")
        for i in range(len(sizes)):
            sizes[i] = int(sizes[i])

        start=0
        pos=0
        decoded_list=[]
        for size in sizes:
            pos = pos + size
            decoded_list.append(words[start:pos])
            start=pos
        return decoded_list