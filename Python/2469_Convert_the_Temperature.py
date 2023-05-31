class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15,(celsius * 9/5) + 32] # return list with the calculated values of kelvin and faren