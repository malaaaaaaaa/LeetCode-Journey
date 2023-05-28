class Solution:
    def isThree(self, n: int) -> bool:
        """
        nsqrt = n**(1/2) # find the square root of n
        if nsqrt % 1 != 0 or n==1: # if the squareroot of n is not a whole number it means it cannot only have three divisors and if special case n==1, it also cannot have three divisors
            return False
        for i in range(2,int(nsqrt)): # for the range of 2 to nsqrt, int must be placed as some numbers will be a float but it will be already returning False
            if int(nsqrt)%i == 0: # if any number from 2 to n sqrt is a factor of nsqrt, return false
                return False
        return True # after both test is done it will mean that n has only three factors
        """
# Thought process, Three Divisors means that it a number a will only have 3 factors.
# The three factors are itself, 1 and the square root of the number eg 9
# 9 = 9 x 1 and 9  = 3 x 3. This also means that the square root of the number must be a prime number.
# The for loop is to check whether nsqrt is a prime or not
        """
        count=0  Count to count how many times it can be divided
        for i in range(1,n+1):
            if n%i==0: # Is i a valid factor
                count+=1 factor count
        if count==3: # if there are only three factors
            return True
        else:return False #  if there are more
        """
        nsqrt = n**(1/2)
        if nsqrt % 1 != 0 or n==1:
            return False
        for i in range(2,int(nsqrt)//2): #Optimized. Floor Divison to return a int. It is to make it slightly faster as the range will be cut in half
            if nsqrt%i == 0:
                return False
        return True