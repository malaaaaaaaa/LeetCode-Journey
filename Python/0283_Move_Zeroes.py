class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for x in range(len(nums)):         #Using Two Pointers i is for 0 and x is for other number
            if nums[x] != 0: # if x is 0, skip
                nums[i], nums[x] = nums[x], nums[i] # if x is a none 0 digit, switch the num at i and num at x
                i += 1 # increase to the next 0

        # Visualising [1,0,2,0,3,4,5]
        # i and x will be switched but it is the same number thus it will still be [1,0,2,0,3,4,5]
        # i will point to the first 0 and x will be pointed to the next 0 too
        # since x is 0 it will skip and go to 2
        # since x is 2, it will switch with i thus becoming [1,2,0,0,3,4,5], i will countinue to point to the first 0 after 2
        # x will go to the next 0 and skip
        # x will go to 3 and switch with the first 0 after two and become [1,2,3,0,0,4,5] and i will increase by 1
        # To easily visualise [1,2,0(1),0(2),3,4,5]
        #                            i       x        
        # after switch     [1,2,3,0(2),0(1),4,5]
        #                          i+1      x+1
        # since x is 4, it will switch and become [1,2,3,4,0(1),0(2),5] and i will increase by 1
        # since x is 5 it will switch and become [1,2,3,4,5,0(2),0(1)]



        """
        A method i find easier to understand but will take longer than the first method
        class Solution:
            def moveZeroes(self, nums: List[int]) -> None:
        
        Do not return anything, modify nums in-place instead.
        
            no0 = nums.count(0)  Find the amount of 0 in the list
            for i in range(no0): Remove the first instance of the 0 and add the 0 into the back
                nums.remove(0)
                nums.append(0)
        """