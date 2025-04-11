import time
class stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return self.item==[]
    def push(self,item):
        self.item.append(item)
    def pop (self):
        return self.item.pop()
    def peek (self):
        return self.item[len(self.item)-1]
    def size (self):
        return len(self.item)
    def display (self):
        return (self.item)
s=stack()
start=time.time()
print(s.is_empty())
print("push operatiin")
s.push(11)
s.push(12)
s.push(13)
print("size:",s.size())
print("peek:",s.peek())
print("pop operation")
print(s.pop())
print(s.pop())
print(s.display())
print("size:",s.size())
end=time.time()
print("runtime of the program is:",end-start)