class Solution:
    def sumBase(self, n: int, k: int) -> int:
        a = 0 # to store the ans
        while n//k: # while n//k is not 0
            a += n%k # add the remainder of n divided by k
            n//=k # mod k
        a += n # add the remainder of n into a
        return a
