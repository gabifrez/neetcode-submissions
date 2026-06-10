class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False;
        open_close = {")": "(", "]": "[", "}": "{"};
        stack = [];
        for element in s:
            if stack and element in open_close:
                if open_close[element] != stack.pop():
                    return False;

            else:
                stack.append(element)
        
        return len(stack) == 0