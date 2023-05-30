class Solution:
    def removeStars(self, s: str) -> str:
        x = []
        for char in s: # every character
            if char == '*': # if the char is a star it will remove the last input character and not add the char into x
                x.pop(len(x)-1)
            else:
                x.append(char) # add the char if it is not a star

        return ''.join(x)  # return x as a string