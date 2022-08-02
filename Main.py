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
   
Range = int(input("Enter the Range of the Stack:"))
s = Stack(Range)
while(1):
    print("Press 1 for Push")
    print("Press 2 for Pop")
    print("Press 3 for Peek")
    print("Press 4 Display\n")

    option = int(input("Enter the Key to Choose:"))
    if(option == 1):
        val = int(input("Enter the Value to Push:"))
        s.Push(val)
    elif(option == 2):
        s.Pop()
    elif(option == 3):
        s.Peek()
    elif(option == 4):
        s.Display()
    else:
        print("You have Pressed the Wrong key:",option)
        if(True):
            val = int(input("Press 10 to stop the Program:"))
            if(val == 10):
                break
            else:
                continue

