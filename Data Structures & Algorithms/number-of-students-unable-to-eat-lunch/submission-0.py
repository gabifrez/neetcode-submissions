class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student = [0,0]
        for element in students:
            student[element]+=1
        for i in range(len(sandwiches)):
            tipe = sandwiches[i]
            student[tipe] -=1
            if student[sandwiches[i]] == -1:
                return student[tipe-1]
        return 0

        