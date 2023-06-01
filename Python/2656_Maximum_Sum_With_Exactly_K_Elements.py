class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums)*k + int((k)*(k-1)/2)

        # since whatever we are removing will be readded back with + 1, we will always take the highest number in the list
        # we will times the highest number by the number of times we will take the num which is k
        # since everytime it will be added back it will be +1, we need to add the sum of k-1 to 1
        # formula for adding all the numbers is x(x+1)/2 where x is the highest number
        # thus since k-1 is the highest number, the formula will be (k-1)*k/2