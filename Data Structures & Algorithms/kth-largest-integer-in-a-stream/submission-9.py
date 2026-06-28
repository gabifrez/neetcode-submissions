class KthLargest:

    def __init__(self, k: int, nums):
        self.array = [0] + nums
        self.k = k + 1
        self.heapping()
        while len(self.array) > self.k:
            self.popping()
    def heapping(self):
        current = (len(self.array) - 1) // 2
        while current > 0:
            i = current
            while 2 * i < len(self.array):
                if 2 * i + 1 < len(self.array) and self.array[i*2 + 1] < self.array[i*2] and self.array[i] > self.array[i*2 + 1]:
                    self.array[i], self.array[i*2+1] = self.array[i*2 + 1], self.array[i]
                    i = i*2 + 1
                elif self.array[i] > self.array[i*2]:
                    self.array[i], self.array[i*2] = self.array[i*2], self.array[i]
                    i = i*2
                else:
                    break
            current -= 1
        return self.array
    def popping(self):
        self.array[1] = self.array.pop()
        self.heapping()
    
    def add(self, value):
        if len(self.array) < self.k:
            self.array.append(value)
        elif self.array[1] < value:
            self.array[1] = value
        self.heapping()
        return self.array[1]
