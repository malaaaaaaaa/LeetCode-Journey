class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = hAlt = 0
        for i in range(len(gain)):
            alt += gain[i]
            if alt > hAlt:
                hAlt = alt
        return hAlt