class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)%3 != 0: # if the sum of the array is not divisible by 3 auto False
            return False
        target = int(sum(arr)/3) # target per part will be the sum of arr divided by 3, we need to int it as if there are times when arr is not divisble by 3 it will return a float
        total = 0 # total sum
        count = 0 # number of times the target has been reached
        for num in arr:
            total += num # add the num to the total
            if total == target: # if the total has reached the target we add the count and reset the total
                count += 1
                total = 0
        return count >= 3 # return true or false if the count is greater than or equal to 3

        # Had trouble understanding why >= 3 and not = 3
        # Special casses for 4 counts such as [0,0,0,0]
        # still can be used as 0+0,0,0 etc
        # Normal cases wont have any extra counts as they need to reach their target before adding a count and if sum(arr) is
        # divisible by 3, means that after finding two parts the last part should equal to the target already.
        