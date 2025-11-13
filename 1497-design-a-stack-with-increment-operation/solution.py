class CustomStack:

    def __init__(self, maxSize: int):
        self.list=[]
        self.n=maxSize

    def push(self, x: int) -> None:
         if len(self.list)<self.n:
            self.list.append(x)

    def pop(self) -> int:
        return -1 if not self.list else self.list.pop()
        

    def increment(self, k: int, val: int) -> None:
        self.list[:k]=[i+val for i in self.list[:k]]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
