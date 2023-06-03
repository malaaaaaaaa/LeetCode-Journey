class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left , right = 0, len(s) - 1 # using two pointers where left is the first and right is the last
        while left<right: # as long as left is not greather than right, as if they are the same there will be no change
            s[left],s[right] = s[right],s[left] # left and right will switch values
            left += 1 # increase to the next value
            right -= 1 # decrease to the next value