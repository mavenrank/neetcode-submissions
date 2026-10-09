class Solution:

    def encode(self, strs: List[str]) -> str:
        #"hello","world"
        # encoded_string=""
        # for word in strs:
        encoded_string="#".join(strs)
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        decoded_list=s.split("#")
        return decoded_list