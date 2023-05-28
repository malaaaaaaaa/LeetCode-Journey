class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = hAlt = 0
        for i in range(len(gain)): 
            alt += gain[i] # the alt will be changed by adding the gain
            if alt > hAlt: # if the alt is higher than the curr highest alt highest alt will be replaced
                hAlt = alt
        return hAlt # return the highest alt aft going through the list gain