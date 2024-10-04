class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Stack:
    def __init__(self):
        self.top = None  
        
    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data
    
if __name__ == "__main__":
    stack = Stack()

    kal = input("Masukkan sebuah kalimat: ")
    for char in kal:
        stack.push(char)
    
    print("Mengeluarkan huruf satu per satu dari stack:")

    pil=0
    while (pil != '3'):
        print("1. Pop")
        print("2. Pop sisanya")
        print("3. Keluar")
        pil = input("Masukkan pilihan : ")
        if (pil=='1'):
            print("Output : " + stack.pop())
        elif (pil=='2'):
            while not stack.is_empty():
                print(stack.pop(), end=' ')
            print()
        elif pil == '3':
            print("Keluar dari program.")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
        
    
