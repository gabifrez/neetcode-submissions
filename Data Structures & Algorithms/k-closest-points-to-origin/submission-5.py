class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dictionary = {}
        values = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            if distance in dictionary:
                dictionary[distance].append(point)
            else:
                values.append(distance)
                dictionary[distance] = [point]
        values.sort()
        answer = []
        for value in values:
            for point in dictionary[value]:
                answer.append(point)
                k-=1
            if k == 0:
                break
        return answer
        

