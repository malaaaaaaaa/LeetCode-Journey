class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no = '' # to store the digit
        for num in digits:
            no += str(num) # change the digit from list to string
        no = str(int(no) + 1) # add the string number into a int and add by 1 and revert back to str
        ans = []
        for num in no:
            ans.append(int(num)) # to make it into a list again
        return ans
