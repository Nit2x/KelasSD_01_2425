class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None
        
    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return None
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data
    
if __name__ == "__main__":
    queue = Queue()

    kal = input("Masukkan sebuah kalimat: ")
    for char in kal:
        queue.enqueue(char)
    
    print("Mengeluarkan huruf satu per satu dari Queue:")

    pil=0
    while (pil != '3'):
        print("1. Dequeue")
        print("2. Dequeue sisanya")
        print("3. Keluar")
        pil = input("Masukkan pilihan : ")
        if (pil=='1'):
            print("Output : " + queue.dequeue())
        elif (pil=='2'):
            while not queue.is_empty():
                print(queue.dequeue(), end=' ')
            print()
        elif pil == '3':
            print("Keluar dari program.")
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
        
    
