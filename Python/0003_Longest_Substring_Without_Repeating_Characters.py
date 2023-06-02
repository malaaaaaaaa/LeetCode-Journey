class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 # to store the lenght of the word
        substring = [] # to store substring

        for char in s: # for each character in s
            while char in substring: # if the chracter is in the substring
                if longest < len(substring):# if the longest stored is lower than the substring length
                    longest = len(substring) # longest will be changed to the subtring now before it is appended
                substring.pop(0) # remove the first letter
            substring.append(char) # only append the letter into the substring when there are no more dupe of it in the substring
        return max(longest,len(substring)) # return either the last len of the substring or the longest stored