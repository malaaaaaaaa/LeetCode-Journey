class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = '' # new string for our new merged word to return and add
        while word1 and word2: # if word1 and word2 has a char it will run otherwise it will be false
            merged += word1[0] # add the first char of the first word
            merged += word2[0] # add the first char of the second word
            word1 = word1[1:] # using slicing, remove the first char from both the words
            word2 = word2[1:] 

        merged += word1 + word2 # add the remaining char from the words into merged as either word1, word2 or both will be empty when the while loop is finished

        return merged # return the merged string