class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        acceptable = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


        while l<r:
            if s[l] not in acceptable:
                l+=1
                continue
            elif s[r] not in acceptable:
                r-= 1
                continue


            if s[l].lower() == s[r].lower():
                l+=1
                r-=1

            else:
                return False

        
                

        return True
        