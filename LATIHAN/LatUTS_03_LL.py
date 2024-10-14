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


def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def hitung_postfiks(infiks):
    stack_hit = Stack()
    for char in infiks: 
        if char.isnumeric(): 
            stack_hit.push(int(char))
        else:
            if is_operator(char):
                c1 = stack_hit.pop()
                c2 = stack_hit.pop()
                
                if char=='+':
                    stack_hit.push(c2+c1)
                if char=='-':
                    stack_hit.push(c2-c1)
                if char=='*':
                    stack_hit.push(c2*c1)
                if char=='/':
                    stack_hit.push(c2/c1)
                if char=='^':
                    stack_hit.push(c2^c1)

    return stack_hit.pop()

postfiks = "29-31*+9-"

postfiks = hitung_postfiks(postfiks)
print("Total: ", postfiks)