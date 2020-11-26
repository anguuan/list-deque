class Deque:
    def __init__(self, initList = None):
        self.data = [None]
        self.head = 1
        if initList:
            self.data.extend(initList)
    
    def __len__(self):
        return len(self.data) - self.head
    
    def __bool__(self):
        return bool(len(self))
    
    def append(self, item):
        self.data.append(item)
    
    def pop(self):
        if not self:
            raise RuntimeError('cannot pop a empty deque')
        return self.data.pop()
    
    def appendLeft(self, item):
        if self.head == 0:
            length = len(self.data)
            self.data.extend([None] * length)
            for i in range(length):
                self.data[i+length] = self.data[i]
                self.data[i] = None
            self.head = length
        self.head -= 1
        self.data[self.head] = item

    def popLeft(self):
        if not self:
            raise RuntimeError('cannot pop a empty deque')
        x = self.data[self.head]
        self.data[self.head] = None
        self.head += 1
        return x
    
    def __getitem__(self, i):
        if isinstance(i, int):
            return self.data[self.head + i]
        elif isinstance(i, slice):
            start = i.start + self.head if i.start else self.head
            stop = i.stop + self.head if i.stop else len(self.data)
            j = slice(start, stop, i.step)
            return self.data[j]
    
    def __setitem__(self, i, item):
        if isinstance(i, int):
            self.data[self.head + i] = item
        elif isinstance(i, slice):
            start = i.start + self.head if i.start else self.head
            stop = i.stop + self.head if i.stop else len(self.data)
            j = slice(start, stop, i.step)
            self.data[j] = item
    
    def __iter__(self):
        return iter(self.data[self.head:])
    
    def __str__(self):
        return str(self.data[self.head:])
    
    __repr__ = __str__

if __name__ == '__main__':
    d = Deque([1,2,3])
    d.appendLeft(4)
    d.appendLeft(5)
    d[1:3] = [6,7]
    for i in d:
        print(i)
    print(len(d))
