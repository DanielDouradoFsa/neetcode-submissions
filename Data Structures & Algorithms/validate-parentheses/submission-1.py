class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        brackets_in_order = []
        for letter in s:
            if letter in close_to_open:#Open bracket
                if brackets_in_order and brackets_in_order[-1]==close_to_open[letter]:
                    brackets_in_order.pop()
                else:
                    return False
            else:#Close bracket
                brackets_in_order.append(letter)
        return len(brackets_in_order)==0
            
                

                
                
        