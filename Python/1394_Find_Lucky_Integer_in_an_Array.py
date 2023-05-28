class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nums = sorted(set(arr), reverse = True) # turn arr into a list to remove duplicates and sort it from highest to lowest as if there are multiple lucky number highest will be returned
        for i in nums: # from highest to lowest
            if i == arr.count(i): # if the number is a lucky number return it
                return i
        return -1 # if there are no lucky number return -1