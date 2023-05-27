class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = 0
        for i in range(len(nums)): 
            diff = target - nums[i] # find the diff needed for each number on the list
            if diff in nums: 
                num1 = nums.index(diff) # if the diff is in the list we find which index it is
                if num1 == i: # to make sure if the diff and number is not the same index on the list
                    continue
                break
        return[num1, i]