class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False;
        open_close = {")": "(", "]": "[", "}": "{"};
        stack = [];
        for element in s:
            if element in open_close:
                if stack and open_close[element] == stack[-1]:
                    stack.pop()
                else:
                    return False;

            else:
                stack.append(element)
        
        return len(stack) == 0