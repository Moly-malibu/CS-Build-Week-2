#from re import sub

class Solution:
    #def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        s = "".join(c for c in s if c.isalnum()).lower()
        
        def ispal(s):
            if len(s) < 2:
                return True

            return s[0] == s[-1] and ispal(s[1:-1])
        
        return ispal(s)

        """
        s = sub(r'[\W_]', '', s).lower() 
        return s == s[::-1]
        """
        
        """
        s = "".join(c for c in s if c.isalnum()).lower()
        
        i0 = 0
        i1 = len(s) - 1 
        
        while i1 > i0:
            if s[i0] != s[i1]:
                return False
            
            i0 += 1
            i1 -= 1
            
        return True
        """
        
        """
        if s == "":
            return True
        
        i0 = 0
        i1 = len(s) - 1 
        
        while i1 > i0:
            if not s[i0].isalnum():
                i0 += 1
                continue
                
            if not s[i1].isalnum():
                i1 -= 1
                continue
                
            if s[i0].lower() != s[i1].lower():
                return False
            
            i0 += 1
            i1 -= 1
            
        return True
        """