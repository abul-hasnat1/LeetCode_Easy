class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        m=x[::-1]
        if x==m:
            return True
        else:
            return False
        
