class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = p2 = 0 # Solved using two pointers

        while len(s) != p1 and len(t) != p2: # p1 has not reached the length of s meaning that if the 1st pointer has not gotten to the end of the string same goes for p2 and t
            if s[p1] == t[p2]: # if p1 s is the same char as p2 t we add the p1 by 1 to move to the next letter
                p1+=1
            p2+=1 # no matter what it must increase by one to move to the next char
        
        return len(s) == p1 # return true or false as it will be false when p1 did not reach the end of s chars