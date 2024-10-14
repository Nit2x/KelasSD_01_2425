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

def infiks_to_postfiks(infiks):
    stack_opr = Stack()
    stack_post = Stack()
    for char in infiks: 
        if char.isalnum(): 
            stack_post.push(char)
        else:
            if char != ' ':
                if char == '(':
                    stack_opr.push(char)
                elif char == ')':
                    while not stack_opr.is_empty() and stack_opr.peek() != '(':
                        stack_post.push(stack_opr.pop())
                    stack_opr.pop()
                else:
                    while not stack_opr.is_empty() and derajat(stack_opr.peek()) >= derajat(char):
                        stack_post.push(stack_opr.pop())
                    stack_opr.push(char)
        # stack_opr.print()
        # stack_post.print()
        
    while not stack_opr.is_empty():
        stack_post.push(stack_opr.pop())
    
    while not stack_post.is_empty():
        stack_opr.push(stack_post.pop())

    postfiks_expression = ''
    while not stack_opr.is_empty():
        postfiks_expression += stack_opr.pop()
    return postfiks_expression

infiks = "5 * 9 + 6 ^ 3 - 6 + 2"

postfiks = infiks_to_postfiks(infiks)
print("Infiks: ", infiks)
print("Postfiks: ", postfiks)