class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort() # To sort the student and seat list to lowest to highest
        students.sort()
        total = 0
        for x,y in zip(seats,students): # for every value of seats and students from lowest to highest we add the abs diff between them to the total
            total += abs(x-y)
        return total
# We dont have to remove the same counts such as it will be the same total
# EG list [1,2,3] = seats [2,3,4] = students
# we could let student 4 move 3 times to 1 and leave 2 and 3 but it will be the same as
# moving 2 to 1, 3 to 2, and 4 to 3.
