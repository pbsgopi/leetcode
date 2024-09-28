class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[]
        self.len=k

    def insertFront(self, value: int) -> bool:
        if len(self.deque)<self.len:
            self.deque.insert(0,value) 
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque)<self.len:
            self.deque.append(value) 
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.deque:
            self.deque=self.deque[1:]
            return True

    def deleteLast(self) -> bool:
        if self.deque:
            self.deque=self.deque[:-1]
            return True

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:return -1


    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:return -1

    def isEmpty(self) -> bool:
        if self.deque:
            return False
        return True

    def isFull(self) -> bool:
        if self.len==len(self.deque):return True