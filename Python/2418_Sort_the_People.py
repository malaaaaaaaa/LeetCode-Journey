class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nameSort = []

        heightSort = sorted(heights, reverse = True) # sorted from highest to lowest
        for x,y in zip(names,heights): # for the names and height
            heightSort[heightSort.index(y)] = x # change the height from the sorted list to their name
        return heightSort # return all their names according to their heights