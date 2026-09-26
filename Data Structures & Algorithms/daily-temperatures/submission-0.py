class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp, index
        answer = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                answer[stack_index] = index - stack_index
            stack.append((temp,index))
        return answer