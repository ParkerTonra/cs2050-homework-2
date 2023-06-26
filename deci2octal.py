class myStack: #myStack class from worksheet 3.1
    def __init__(self):
        self.myList = []

    def isEmpty(self):
        return not bool(self.myList)

    def push(self, item): 
      self.myList.append(item)

    def pop(self):
      return self.myList.pop()

    def peek(self):
      return self.myList[-1]

    def size(self):
      return len(self.myList)

def deci2octal(deci):
    stack = myStack()  # create a stack object
    # if decimal number = 0, octal number = 0 (push)
    if deci < 0:
       return "This program works only for positive integers. Please try again."
       

    if deci == 0:
        stack.push(deci)

    while deci > 0:
        r = deci % 8  # calculate remainder
        stack.push(r)  # push remainder to the stack
        deci = deci // 8  # update decimal by dividing it by 8

    octal = ""
    while stack.isEmpty() == False:
        octal = octal + str(stack.pop())  # pop digits from the stack

    return octal

print(deci2octal(42))
print(deci2octal(444))
print(deci2octal(0))
print(deci2octal(-27))