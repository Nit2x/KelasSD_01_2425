class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deret(n, nilai=None, index=1, prev=None, head=None):
    if nilai==None:
        nilai=n
    else:
        if (index % 2==0):
            nilai = nilai * index
        else:
            nilai = nilai // index

    if index > n:
        return head
    else:
        new_node = Node(nilai)
        if prev is None:
            head = new_node
        else:
            prev.next = new_node
        prev = new_node
        return deret(n, nilai, index + 1, prev, head)

def print_linked_list(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next
    print()

# Contoh penggunaan
n = 4
result = deret(n)
print_linked_list(result)

n = 7
result = deret(n)
print_linked_list(result)  