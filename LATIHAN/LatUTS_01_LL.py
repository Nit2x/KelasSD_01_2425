class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.is_empty():
            item = self.top.data
            self.top = self.top.next
            return item

    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if not self.is_empty():
            return self.top.data
    
    def print(self):
        temp = self.top
        while (temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()

def derajat(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    return 0

def infiks_to_prefiks(infiks):
    stack_opr = Stack()
    stack_pre = Stack()
    for char in infiks[::-1]: 
        if char.isalnum(): 
            stack_pre.push(char)
        else:
            if char != ' ':
                if char == ')':
                    stack_opr.push(char)
                elif char == '(':
                    while not stack_opr.is_empty() and stack_opr.peek() != ')':
                        stack_pre.push(stack_opr.pop())
                    stack_opr.pop()
                else:
                    while not stack_opr.is_empty() and derajat(stack_opr.peek()) > derajat(char):
                        stack_pre.push(stack_opr.pop())
                    stack_opr.push(char)
        # stack_opr.print()
        # stack_pre.print()
        
    while not stack_opr.is_empty():
        stack_pre.push(stack_opr.pop())
    prefiks_expression = ''
    while not stack_pre.is_empty():
        prefiks_expression += stack_pre.pop()
    return prefiks_expression

infiks = "A - B ^ C / (D * (E + F))"

prefiks = infiks_to_prefiks(infiks)
print("Infiks: ", infiks)
print("Prefiks: ", prefiks)