class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()

        i = self.size
        self.size += 1
        self.arr[i] = n


    def popback(self) -> int:
        i = self.size - 1
        res = self.arr[i]
        self.size -= 1
        return res
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
