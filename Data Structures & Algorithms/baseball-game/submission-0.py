class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0
        stack = []

        for operation in operations:
            if operation == "D":
                stack.append(stack[-1]*2)
                result += stack[-1]
            elif operation == "C":
                result-=stack.pop()
            elif operation == "+":
                value = stack[-1] + stack[-2]
                result += value
                stack.append(value)
            else:
                number = int(operation)
                result += number
                stack.append(number)

        return result