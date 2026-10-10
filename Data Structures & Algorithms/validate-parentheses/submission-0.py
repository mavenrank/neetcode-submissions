class Solution:
    def isValid(self, s: str) -> bool:
        pairs=["[]", "()", "{}"]

        while True:
            removed=False
            for pair in pairs:
                pos=s.find(pair)
                if pos !=-1:
                    s=s[:pos]+s[pos+2:]
                    removed=True
                    break


            if not removed:
                return False
            if len(s) == 0:
                return True    

