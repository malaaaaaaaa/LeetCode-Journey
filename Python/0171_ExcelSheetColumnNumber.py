class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1 # First time using ord and did not know what it did until reading about it
            result = result*26 + value
        return result