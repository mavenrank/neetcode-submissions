class Solution:
    def isPalindrome(self, s: str) -> bool:
        front=0
        rear=len(s)-1
        isPalindrome=True
        while (front<rear):
            if s[front].isalnum() != True:
                front+=1
            elif s[rear].isalnum() != True:
                rear-=1
            else:
                if s[front].lower()!=s[rear].lower():
                    return False
                
                isPalindrome &= True
                front+=1
                rear-=1
        
        return True