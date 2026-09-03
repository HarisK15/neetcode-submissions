class Solution:
    def isPalindrome(self, s: str) -> bool:
        acceptedchar = "ABCDESFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

        l,r = 0, len(s)-1

        while l<r:
            if s[l] not in acceptedchar:
                l+=1
            elif s[r] not in acceptedchar:
                r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
                

        return True


       
                
