class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0 # using two pointers
        while p1 < len(nums1) and p2 < len(nums2): # as long as none of the pointers are out of index
            if nums1[p1] < nums2[p2]: # if num1 is smaller than num2
                p1 += 1 # num1 increases
            elif nums1[p1] > nums2[p2]: # if num2 is smaller than num1
                p2 += 1 # num2 increases
            else:
                return nums1[p1] # return if both are the same
        return -1   # return if the list has been gone through
        # since both num1 and num2 are in non decreasing order we can do this as we will not skip anything