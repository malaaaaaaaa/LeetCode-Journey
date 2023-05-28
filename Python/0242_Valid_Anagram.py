class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(t) == sorted(s): # If sorted t is the same as a sorted s it means they have the same characters thus meaning they are an anagram
            return True
        return False