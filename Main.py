class Stack():
    def __init__(self,Range):
        self.Array = list()
        self.Range = Range
        self.top = -1
    def Push(self,val):
        self.top += 1
        self.Array.append(val)
        if(len(self.Array) > self.Range):
            print("Overflow is occured at this point:",self.top)
            print("\n")
    def Pop(self):
        if(self.top == -1):
            print("Stack is a Empty")
            print("Underflow condition is occured ")
            print("\n")
        else:
            self.top -= 1
            self.Array.pop()
    def Peek(self):
        print("The Latest Value of the Stack is :",self.Array[self.top])
        print("\n")
    def Display(self):
        print("The Array of the Stack is :",self.Array)
        print("\n")
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

