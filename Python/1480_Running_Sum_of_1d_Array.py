class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [] # to store our ans
        rSum = 0 # running sum
        for i in nums: # for each number in the num list
            rSum += i # running sum increases by the number
            ans.append(rSum) # add the running sum to list
        return ans