class Stack:
    def __init__(self):
        self.lst = []
    def IsEmpty(self):
        if len(self.lst) == 0:
            return True
        return False
    def Top(self):
        return self.lst[len(self.lst) -  1]
    def Push(self, val):
        self.lst.append(val)
    def Pop(self):
        self.lst.pop()
    def Size(self):
        return len(self.lst)