class MyCalendarTwo:

    def __init__(self):
        self.l=defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.l[start]+=1
        self.l[end]-=1
        c=0
        for i in sorted(self.l.keys()):
            c+=self.l[i]
            if c>=3:
                self.l[start]-=1
                self.l[end]+=1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)