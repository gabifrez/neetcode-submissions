class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False;
        open_b = ['(', '[', '{'];
        close_b = [')', ']', '}'];
        teams = ["()", "[]", "{}"];
        stack = [];
        for element in s:
            if element in open_b:
                stack.append(element);
            if element in close_b:
                if len(stack) == 0:
                    return False;
                if stack.pop() + element not in teams:
                    return False;
        if len(stack) ==0:
            return True;
        else:
            return False
        