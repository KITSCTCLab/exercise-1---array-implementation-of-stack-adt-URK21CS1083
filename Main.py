import os
class Stack():
    """The class implements a stack"""
    def __init__(self,Range):
        self.items = []
        self.size=Range
        
    def is_empty(self):
        return len(self.items)==0
    
    def is_full(self):
        return len(self.items)==self.size
    
    def Push(self,data):
        if not self.is_full():
            self.items.append(data)
            
    def Pop(self):
        if not self.is_empty():
            self.items.pop(-1)
            
    def status(self):
        for elements in self.items:
            print(elements)
   
Range,queries = map(int, input().rstrip().split())
stack = Stack(Range)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
